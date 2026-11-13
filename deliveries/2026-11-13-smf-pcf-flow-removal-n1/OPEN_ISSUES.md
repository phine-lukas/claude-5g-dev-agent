# Open issues — 2026-11-13-smf-pcf-flow-removal-n1

## Untested in the cloud

1. **Nothing above T1 ran here.** `oai-cn5g-fed` is not in this session, and
   the VM has no docker daemon, so T2 and T3 could not run. The end-to-end
   claim — gNB releases the DRBs, UE deletes the QoS rules — is **not verified
   by this delivery**. TESTING.md L1 has the exact local steps.

2. **The N1 and N2 builders have no unit test.** `smf_n1::create_n1_pdu_session_
   modification_command()` and the `smf_n2` builder both reach into the global
   `smf_app_inst` for the SMF context, so they cannot be constructed in the test
   binary as it stands. The new tests assemble the same IEs directly, which
   covers the encoding but **not** the builders' own logic — for instance that
   both overloads really do pass the released flows through. Making those
   testable means injecting the context, which is a refactor well beyond this
   fix.

3. **`smf_context::handle_pdu_session_modification_network_requested()` has no
   unit test** for the same reason (global context + ITTI). The container
   logic added by commit #2 is therefore only covered by inspection and by the
   local run.

## Assumptions

4. **The delete-rule shape changes bytes on the wire to the UE.** A delete rule
   goes from 6 octets (two of them uninitialised garbage) to the 4 the spec
   describes. Upstream OAI nrUE `develop` handles the delete operation, but any
   UE that happened to tolerate the old encoding is untested here.

5. **The ENCODE macro change is library-wide.** `common_defs.h` is vendored by
   the AMF and UPF as well. A scan of the SMF tree found exactly three unbraced
   conditional call sites, all fixed in the same commit, so within this repo the
   change is inert everywhere else. **The AMF and UPF trees were not scanned**,
   because their `common-src` is pinned separately. Before bumping the submodule
   there, run the same scan:

   ```bash
   grep -rn -B1 -E '^\s*(ENCODE|DECODE)_U(8|16|32)\(' --include=*.cpp src/ \
     | grep -B0 -A1 'if (' | grep -v '{'
   ```

   Any site it reports was relying on the unconditional `size +=` and needs
   reading before the bump.

6. **`_5gsNetworkFeatureSupport::Encode()` behaviour changes.** It had the same
   unbraced-macro defect for its octet 4, so it over-reported by one octet
   whenever the condition was false. It is an AMF-side IE (Registration Accept),
   not used by the SMF, and it is now correct — but that is a behaviour change
   this delivery makes outside the reported defect set, worth a look from
   whoever owns the AMF.

## Known gaps, not addressed

7. **The AMF drops the whole transfer when a declared container is empty**, and
   answers 200 `N1_N2_TRANSFER_INITIATED` while doing so, with no log line
   (`oai-cn5g-amf`, `src/sbi/amf_http2_server.cpp`, the
   `parts[n1_content_id].body.size() == 0` path). The SMF no longer triggers it,
   but the silent drop remains for any other caller. Separate AMF issue.

8. **UEs in CM-IDLE** get no Modification Command at all; the SMF logs a warning
   and sends nothing (`src/smf_app/smf_procedure.cpp`, already marked TODO).
   Declared out of scope in the task.

9. **The UPF update step after a release-only modify.** The SMF tolerates an
   empty QFI list in the gNB's response (`src/smf_app/smf_procedure.cpp` around
   line 1608) but then copies the gNB tunnel ID from that response onto the
   downlink edges. A response carrying no tunnel info would write zero there.
   Not reproduced and not changed — watch for it during L1, as the task
   description asks.

10. **`googletest-tools` is not installable on Ubuntu 24.04**, although the
    repo's `docker/Dockerfile.smf.ubuntu` `checks` stage asks for it alongside
    `libgtest-dev` and `libgmock-dev`. It is not needed for the build; the
    package simply no longer exists. Harmless in Docker only because that stage
    installs the other two first. Worth dropping from the Dockerfile.

11. **`build_smf --install-deps` does not install GoogleTest**, so a native
    `build_smf --tests` fails at `#include <gtest/gtest.h>` on a fresh machine.
    Install `libgtest-dev libgmock-dev` first. Noted in the toolkit's `oai-cn`
    skill in the same push as this delivery.
