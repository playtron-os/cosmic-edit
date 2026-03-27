Name:           cosmic-edit
Epoch:          1
Version: 1.1.0
Release:        1%{?dist}
Summary:        Text Editor (Playtron fork)

License:        GPL-3.0-only
URL:            https://github.com/pop-os/cosmic-edit
Source0:        %{name}-%{_arch}.tar.gz

# No BuildRequires - binary is pre-built

Requires:       (cosmic-icon-theme >= 1.0.0 with cosmic-icon-theme < 1.1.0)

%description
Text editor for the COSMIC desktop environment.
A libcosmic-based text editor with syntax highlighting and GPU acceleration.

%prep
%autosetup -n %{name} -p1

%build

%install
install -Dm0755 "usr/bin/cosmic-edit" "%{buildroot}%{_bindir}/cosmic-edit"
install -Dm0644 "usr/share/applications/com.system76.CosmicEdit.desktop" "%{buildroot}%{_datadir}/applications/com.system76.CosmicEdit.desktop"
install -Dm0644 "usr/share/metainfo/com.system76.CosmicEdit.metainfo.xml" "%{buildroot}%{_datadir}/metainfo/com.system76.CosmicEdit.metainfo.xml"
install -Dm0644 "usr/share/licenses/cosmic-edit/LICENSE" "%{buildroot}%{_datadir}/licenses/cosmic-edit/LICENSE"

# Install icons
install -Dm0644 "usr/share/icons/hicolor/16x16/apps/com.system76.CosmicEdit.svg" "%{buildroot}%{_datadir}/icons/hicolor/16x16/apps/com.system76.CosmicEdit.svg"
install -Dm0644 "usr/share/icons/hicolor/24x24/apps/com.system76.CosmicEdit.svg" "%{buildroot}%{_datadir}/icons/hicolor/24x24/apps/com.system76.CosmicEdit.svg"
install -Dm0644 "usr/share/icons/hicolor/32x32/apps/com.system76.CosmicEdit.svg" "%{buildroot}%{_datadir}/icons/hicolor/32x32/apps/com.system76.CosmicEdit.svg"
install -Dm0644 "usr/share/icons/hicolor/48x48/apps/com.system76.CosmicEdit.svg" "%{buildroot}%{_datadir}/icons/hicolor/48x48/apps/com.system76.CosmicEdit.svg"
install -Dm0644 "usr/share/icons/hicolor/64x64/apps/com.system76.CosmicEdit.svg" "%{buildroot}%{_datadir}/icons/hicolor/64x64/apps/com.system76.CosmicEdit.svg"
install -Dm0644 "usr/share/icons/hicolor/128x128/apps/com.system76.CosmicEdit.svg" "%{buildroot}%{_datadir}/icons/hicolor/128x128/apps/com.system76.CosmicEdit.svg"
install -Dm0644 "usr/share/icons/hicolor/256x256/apps/com.system76.CosmicEdit.svg" "%{buildroot}%{_datadir}/icons/hicolor/256x256/apps/com.system76.CosmicEdit.svg"

%files
%license %{_datadir}/licenses/cosmic-edit/LICENSE
%{_bindir}/cosmic-edit
%{_datadir}/applications/com.system76.CosmicEdit.desktop
%{_datadir}/metainfo/com.system76.CosmicEdit.metainfo.xml
%{_datadir}/icons/hicolor/*/apps/com.system76.CosmicEdit.svg

%changelog
* Thu Mar 27 2026 Playtron <dev@playtron.one> - 1.0.8-1
- Initial RPM package
