#!/usr/bin/env bash
# What can this machine actually run? Used in Phase 1 of /implement-feature to
# decide which test tiers (T0-T3) are realistic here and which move to local
# testing.
#
#   probe_env.sh            # human-readable report
#   probe_env.sh --json     # same facts as JSON on stdout
#
# Every probe is bounded and failure-tolerant: this script never exits non-zero
# because a capability is missing — that IS the result.

set -u

JSON=0
[ "${1:-}" = "--json" ] && JSON=1

declare -A R=()   # key -> value (strings; "yes"/"no" for booleans)

put() { R["$1"]="$2"; }

have() { command -v "$1" >/dev/null 2>&1; }

yesno() { if "$@" >/dev/null 2>&1; then echo yes; else echo no; fi; }

# ---------------------------------------------------------------- resources --
put cores "$(nproc 2>/dev/null || echo 0)"
put ram_mb "$(awk '/MemTotal/ {printf "%d", $2/1024}' /proc/meminfo 2>/dev/null || echo 0)"
put ram_available_mb "$(awk '/MemAvailable/ {printf "%d", $2/1024}' /proc/meminfo 2>/dev/null || echo 0)"
put disk_cwd_free_gb "$(df -BG --output=avail . 2>/dev/null | tail -1 | tr -dc '0-9' || echo 0)"
put disk_tmp_free_gb "$(df -BG --output=avail /tmp 2>/dev/null | tail -1 | tr -dc '0-9' || echo 0)"
put kernel "$(uname -r 2>/dev/null || echo unknown)"
put os "$( (. /etc/os-release 2>/dev/null && echo "$PRETTY_NAME") || echo unknown)"
put arch "$(uname -m 2>/dev/null || echo unknown)"

# ------------------------------------------------------------- privileges ----
put root "$([ "$(id -u)" -eq 0 ] && echo yes || echo no)"
put sudo_nopasswd "$(yesno sudo -n true)"
put in_container "$([ -f /.dockerenv ] || grep -qE '(docker|containerd|lxc)' /proc/1/cgroup 2>/dev/null && echo yes || echo no)"

# ----------------------------------------------------------------- docker ----
put docker_client "$(yesno have docker)"
put docker_daemon no
put docker_compose no
put docker_run no
put docker_privileged no
put docker_host_network no
if have docker && timeout 25 docker info >/dev/null 2>&1; then
  put docker_daemon yes
  put docker_version "$(docker version --format '{{.Server.Version}}' 2>/dev/null || echo unknown)"
  timeout 20 docker compose version >/dev/null 2>&1 && put docker_compose yes
  # Prefer an image that is already cached; fall back to hello-world.
  img="$(docker images --format '{{.Repository}}:{{.Tag}}' 2>/dev/null | grep -vE '<none>' | head -1)"
  probe_img="${img:-hello-world}"
  if timeout 120 docker run --rm "$probe_img" true >/dev/null 2>&1 \
     || timeout 120 docker run --rm hello-world >/dev/null 2>&1; then
    put docker_run yes
    probe_img="${img:-hello-world}"
    timeout 120 docker run --rm --privileged "$probe_img" true >/dev/null 2>&1 && put docker_privileged yes
    timeout 120 docker run --rm --network host "$probe_img" true >/dev/null 2>&1 && put docker_host_network yes
  fi
fi

# -------------------------------------------------------- kernel features ----
# /dev/net/tun: needed by the UPF (GTP-U tunnel) and the OAI nrUE (oaitun_ue*).
put tun no
if [ -c /dev/net/tun ]; then
  if python3 - <<'PY' >/dev/null 2>&1
import fcntl, struct, os
TUNSETIFF, IFF_TUN, IFF_NO_PI = 0x400454ca, 0x0001, 0x1000
fd = os.open("/dev/net/tun", os.O_RDWR)
try:
    fcntl.ioctl(fd, TUNSETIFF, struct.pack("16sH", b"probe%d", IFF_TUN | IFF_NO_PI))
finally:
    os.close(fd)
PY
  then put tun yes; else put tun "device-present-but-not-usable"; fi
fi

# SCTP: NGAP (gNB <-> AMF) and F1AP in split deployments ride on it.
put sctp "$(python3 - <<'PY' >/dev/null 2>&1 && echo yes || echo no
import socket
socket.socket(socket.AF_INET, socket.SOCK_STREAM, 132).close()
PY
)"

# Network namespaces: many testbed and CI setups need them.
put netns "$(yesno unshare --net --user --map-root-user true)"

# sysctl writes (ip_forward) — UPF/MB-UPF forwarding setups need this.
put sysctl_write "$( ( [ -w /proc/sys/net/ipv4/ip_forward ] || sudo -n test -w /proc/sys/net/ipv4/ip_forward ) >/dev/null 2>&1 && echo yes || echo no)"

# eBPF/TC (the testbed's PTM-to-PTP program needs it).
put bpf_tool "$(yesno have bpftool)"

# ---------------------------------------------------------------- network ----
reach() { if timeout 8 curl -sS -o /dev/null -m 7 "$1" >/dev/null 2>&1; then echo yes; else echo no; fi; }
put net_github "$(reach https://github.com)"
put net_3gpp "$(reach https://www.3gpp.org/ftp/Specs/archive/)"
put net_docker_registry "$(reach https://registry-1.docker.io/v2/)"
put net_gitlab_eurecom "$(reach https://gitlab.eurecom.fr)"

# ------------------------------------------------------------------ tools ----
version_of() { have "$1" && "$@" 2>&1 | head -1 | tr -d '\r' || echo "-"; }
put tool_cmake "$(version_of cmake --version)"
put tool_ninja "$(version_of ninja --version)"
put tool_meson "$(version_of meson --version)"
put tool_gcc "$(version_of gcc --version)"
put tool_clang "$(version_of clang --version)"
put tool_python3 "$(version_of python3 --version)"
put tool_pandoc "$(version_of pandoc --version)"
put tool_robot "$(version_of robot --version)"
put tool_git "$(version_of git --version)"
put tool_tshark "$(version_of tshark --version)"
put tool_clang_format "$(version_of clang-format --version)"

# ------------------------------------------------------------ tier verdict ---
cores="${R[cores]}"; ram="${R[ram_mb]}"; disk="${R[disk_cwd_free_gb]}"
[ -z "$cores" ] && cores=0
[ -z "$ram" ] && ram=0
[ -z "$disk" ] && disk=0

# T0 build
if [ "${R[tool_cmake]}" != "-" ] && [ "$cores" -ge 2 ] && [ "$disk" -ge 10 ]; then
  put verdict_T0 "CAN RUN"; put verdict_T0_why "cmake present, ${cores} cores, ${disk} GB free"
elif [ "${R[tool_cmake]}" = "-" ]; then
  put verdict_T0 "MAYBE"; put verdict_T0_why "no cmake yet — install build deps first"
else
  put verdict_T0 "MAYBE"; put verdict_T0_why "tight resources (${cores} cores, ${disk} GB free); builds may be slow or run out of disk"
fi

# T1 unit tests
if [ "${R[verdict_T0]}" = "CAN RUN" ]; then
  put verdict_T1 "CAN RUN"; put verdict_T1_why "unit tests only need the build to succeed"
else
  put verdict_T1 "MAYBE"; put verdict_T1_why "depends on T0"
fi

# T2 component/integration without RF
if [ "$ram" -ge 4000 ] && [ "${R[verdict_T0]}" = "CAN RUN" ]; then
  put verdict_T2 "CAN RUN"; put verdict_T2_why "${ram} MB RAM; simulators and robot suites fit"
else
  put verdict_T2 "MAYBE"; put verdict_T2_why "only ${ram} MB RAM or no working build"
fi

# T3 container end-to-end (opt-in)
if [ "${R[docker_run]}" = "yes" ] && [ "${R[docker_compose]}" = "yes" ] && [ "${R[tun]}" = "yes" ] \
   && [ "$ram" -ge 8000 ] && [ "$cores" -ge 4 ] && [ "$disk" -ge 30 ]; then
  put verdict_T3 "CAN RUN"; put verdict_T3_why "docker+compose, usable TUN, ${cores} cores / ${ram} MB / ${disk} GB"
elif [ "${R[docker_run]}" != "yes" ]; then
  put verdict_T3 "NO"; put verdict_T3_why "no usable docker daemon"
elif [ "${R[tun]}" != "yes" ]; then
  put verdict_T3 "NO"; put verdict_T3_why "/dev/net/tun not usable — UPF and nrUE tunnels cannot come up"
elif [ "${R[docker_compose]}" != "yes" ]; then
  put verdict_T3 "NO"; put verdict_T3_why "docker compose plugin missing"
else
  put verdict_T3 "MAYBE"; put verdict_T3_why "docker works but resources are tight (${cores} cores / ${ram} MB / ${disk} GB)"
fi

put verdict_T4 "NO"
put verdict_T4_why "testbed/RF/hardware is always local, by design"

# ----------------------------------------------------------------- output ----
if [ "$JSON" -eq 1 ]; then
  # Emit JSON without depending on python: every value is a plain string.
  {
    printf '{\n'
    first=1
    for k in $(printf '%s\n' "${!R[@]}" | sort); do
      v="${R[$k]}"
      v="${v//\\/\\\\}"; v="${v//\"/\\\"}"; v="${v//$'\n'/ }"; v="${v//$'\t'/ }"
      [ $first -eq 1 ] && first=0 || printf ',\n'
      printf '  "%s": "%s"' "$k" "$v"
    done
    printf '\n}\n'
  }
  exit 0
fi

section() { printf '\n=== %s\n' "$1"; }
row() { printf '  %-24s %s\n' "$1" "$2"; }

printf 'probe_env — %s (%s, %s)\n' "${R[os]}" "${R[arch]}" "${R[kernel]}"

section "Resources"
row cores "${R[cores]}"
row "RAM (total/avail MB)" "${R[ram_mb]} / ${R[ram_available_mb]}"
row "free disk cwd / tmp" "${R[disk_cwd_free_gb]} GB / ${R[disk_tmp_free_gb]} GB"

section "Privileges"
row root "${R[root]}"
row "passwordless sudo" "${R[sudo_nopasswd]}"
row "inside a container" "${R[in_container]}"

section "Docker"
row client "${R[docker_client]}"
row "daemon reachable" "${R[docker_daemon]}"
row "compose plugin" "${R[docker_compose]}"
row "can run a container" "${R[docker_run]}"
row "--privileged works" "${R[docker_privileged]}"
row "host networking" "${R[docker_host_network]}"

section "Kernel features"
row "/dev/net/tun usable" "${R[tun]}"
row "SCTP sockets" "${R[sctp]}"
row "network namespaces" "${R[netns]}"
row "sysctl writable" "${R[sysctl_write]}"
row bpftool "${R[bpf_tool]}"

section "Network"
row github.com "${R[net_github]}"
row www.3gpp.org "${R[net_3gpp]}"
row "docker registry" "${R[net_docker_registry]}"
row gitlab.eurecom.fr "${R[net_gitlab_eurecom]}"

section "Tools"
for t in cmake ninja meson gcc clang python3 pandoc robot git tshark clang_format; do
  row "$t" "${R[tool_$t]}"
done

section "Tier verdict"
for t in T0 T1 T2 T3 T4; do
  printf '  %-4s %-8s %s\n' "$t" "${R[verdict_$t]}" "${R[verdict_${t}_why]}"
done
printf '\n  T3 is opt-in: it runs only when the task says E2E (see implement-feature Phase 4).\n'

exit 0
