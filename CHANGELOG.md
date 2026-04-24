## [1.1.2](https://github.com/playtron-os/cosmic-edit/compare/v1.1.1...v1.1.2) (2026-04-24)


### Bug Fixes

* update libcosmic ([b1a92dd](https://github.com/playtron-os/cosmic-edit/commit/b1a92ddf773c2caeb98c1e1a87acadfe9bfca8d5))

## [1.1.1](https://github.com/playtron-os/cosmic-edit/compare/v1.1.0...v1.1.1) (2026-04-09)


### Bug Fixes

* update icons ([ec8d62f](https://github.com/playtron-os/cosmic-edit/commit/ec8d62fb432a997228fbb70ed0a8ba50b58525f4))

# [1.1.0](https://github.com/playtron-os/cosmic-edit/compare/v1.0.0...v1.1.0) (2026-03-27)


### Bug Fixes

* releaserc config ([888ee5b](https://github.com/playtron-os/cosmic-edit/commit/888ee5bacb30785905d4c0f23a12a4ad09aee6d2))


### Features

* unpin iced versions ([9af2361](https://github.com/playtron-os/cosmic-edit/commit/9af23610d0ec942c3097e5e8eb6b9598390d293a))

# 1.0.0 (2026-03-27)


### Bug Fixes

* **322:** fix undo/redo after reverting all changes ([18f6bc4](https://github.com/playtron-os/cosmic-edit/commit/18f6bc4e74eaa5df0485ace4230924572b638e68))
* **context menu:** use radius from theme ([740692d](https://github.com/playtron-os/cosmic-edit/commit/740692d6cf0997c6f9defe09590deaaa5bfba38d))
* **cosmic-text:** pin cosmic-text to b017d7c (via cosmic-term issue [#508](https://github.com/playtron-os/cosmic-edit/issues/508)) ([3e167a4](https://github.com/playtron-os/cosmic-edit/commit/3e167a401e79c8daf3b62b3bb5c16ba531cda944))
* **cosmic-text:** unpin due to upstream revert ([b74cb31](https://github.com/playtron-os/cosmic-edit/commit/b74cb313c55eae94c7c0e8678a4714aa32cf0ba8))
* **debian:** add libxkbcommon-dev ([f5238e1](https://github.com/playtron-os/cosmic-edit/commit/f5238e19b43b21bc5d06d6fc4108256ebce51243))
* enable dbus-config on libcosmic to fix theme not updating ([614c827](https://github.com/playtron-os/cosmic-edit/commit/614c827710808add26aa61021fc239dad7a24265))
* focus find on window focus if text box did not have focus ([73446cd](https://github.com/playtron-os/cosmic-edit/commit/73446cdafc99d45a5b7c1eb8ba179e4201c22900))
* focus the text box when the window gains focus ([cfebad1](https://github.com/playtron-os/cosmic-edit/commit/cfebad159f68e042fdfc6e812d9e8c35c14290eb))
* handle space input as text ([c9ebbd5](https://github.com/playtron-os/cosmic-edit/commit/c9ebbd59b02fda51434bd6669860ddf273552ea2))
* improve font rendering on light theme w/ iced web-colors feature ([7d8f412](https://github.com/playtron-os/cosmic-edit/commit/7d8f4121b9d8cb7c723b9e75bac80f2df45011b7))
* issues with merging from master ([5bbd700](https://github.com/playtron-os/cosmic-edit/commit/5bbd7002e23aabbb7e56069312936611c4080de3))
* **l18n:** Ensure COSMIC is properly cased ([bd80ac7](https://github.com/playtron-os/cosmic-edit/commit/bd80ac7e093c7c6dd283c0ad31513902a743a8ad))
* **libcosmic:** add x11 wgpu device detection to fix crash on NVIDIA desktops ([6e8d212](https://github.com/playtron-os/cosmic-edit/commit/6e8d212ab9a62ddfe3f7914e36e96be1c2430459))
* **libcosmic:** double-click to maximize ([4b176d7](https://github.com/playtron-os/cosmic-edit/commit/4b176d77d398695e40d1f66d40b8a7b7caa772bd))
* **libcosmic:** enable dbus-config only on Linux targets ([c125d5c](https://github.com/playtron-os/cosmic-edit/commit/c125d5c95190aa51c548e74a0a209b052af1206e))
* **libcosmic:** input focus lost on click of header bar ([33d6522](https://github.com/playtron-os/cosmic-edit/commit/33d6522438838e53472d5e98fe23dbd07e6990f1))
* **libcosmic:** theme subscription ([bd5009a](https://github.com/playtron-os/cosmic-edit/commit/bd5009ababd584beb401d955359d94f54229f44d))
* paginated tab button fixes ([8d680f0](https://github.com/playtron-os/cosmic-edit/commit/8d680f0221c48b658ee9f266a3ac57d10ca60b07))
* text input copy paste ([e94564e](https://github.com/playtron-os/cosmic-edit/commit/e94564ec589de3690472981d58d47eefc8971273))
* Unsaved changes should be dialogs ([93e993d](https://github.com/playtron-os/cosmic-edit/commit/93e993d72eb7092f2f73ff6e7f7f93235749b92e)), closes [#174](https://github.com/playtron-os/cosmic-edit/issues/174)
* update deps ([8d16f08](https://github.com/playtron-os/cosmic-edit/commit/8d16f0881631280b34d7b9cbda097b1cb31ebcd3))
* update libcosmic ([3e4a2b2](https://github.com/playtron-os/cosmic-edit/commit/3e4a2b24e6cb44fc635f794285df14f9195f9242))
* update libcosmic ([2d6d2d3](https://github.com/playtron-os/cosmic-edit/commit/2d6d2d381ef2ef7518bb5703abe4bb6a584800d2))


### Features

* improve tab title for mod.rs files ([0581f96](https://github.com/playtron-os/cosmic-edit/commit/0581f96f4614a8b53f52de880a2d9358c7000408))
* menubar popups ([c47c12f](https://github.com/playtron-os/cosmic-edit/commit/c47c12fe17d21aef8b1b0c6819e09106189c19a3))
* rebase libcosmic onto iced 0.14 ([6326f65](https://github.com/playtron-os/cosmic-edit/commit/6326f65d84cd696dceb5c31ebb63842cd756051d))
* remove cosmic from app name ([6d5fa20](https://github.com/playtron-os/cosmic-edit/commit/6d5fa20b84c9439c94b43b281d7e737b7975a90e))
* responsive menu ([9336731](https://github.com/playtron-os/cosmic-edit/commit/9336731c7d9c90b067cbf1b4cab8a5b4d234af42))
* tab dnd ([2b90abd](https://github.com/playtron-os/cosmic-edit/commit/2b90abdde93f6e7ca96072dcd94e11ce7449de9b))
* tab pagination and variable-button widths ([7a70472](https://github.com/playtron-os/cosmic-edit/commit/7a70472572f7018cfe7a38b987b922a7e15cd8e3))
* **text_box:** add CTRL+<backspace> and CTRL+<delete> keybinds (delete left/right word) ([#353](https://github.com/playtron-os/cosmic-edit/issues/353)) ([40a5465](https://github.com/playtron-os/cosmic-edit/commit/40a54654dce89af14e9f2f403b30076b3187525f))
* use xdg file picker dialog instead of cosmic-files ([2493a19](https://github.com/playtron-os/cosmic-edit/commit/2493a195589c56f49a1facc0d86d3f249891ef0c))


### Performance Improvements

* optimized cosmic-freedesktop-icons ([a245aa9](https://github.com/playtron-os/cosmic-edit/commit/a245aa9fcb1ab0aa75f6538a69b9c223ba3deef3))
* reduce disk io when updating config values. ([f97b4fe](https://github.com/playtron-os/cosmic-edit/commit/f97b4fe76c6cc1e7cacaae25e8c44ff4e25360e5))


### Reverts

* Revert "Added additional languages for wrap-around text in find menu" ([18554f3](https://github.com/playtron-os/cosmic-edit/commit/18554f3ac732786e10a7724167cb297d1a83e584))
