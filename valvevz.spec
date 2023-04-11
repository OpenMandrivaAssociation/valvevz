%global upstream OpenMandrivaSoftware
%global gitbase  https://github.com

Summary:  Decompresses Valve's ".zip.vz" files
Name:     valvevz
Version:  1.0
Release:  1
License:  GPLv3
Group:    Archiving/Compression
Url:      https://%{upstream}.github.io/%{name}
Source0:  %{gitbase}/%{upstream}/%{name}/archive/refs/tags/v%{version}.tar.gz

%description
Decompresses Valve's ".zip.vz" files.

%prep
%autosetup
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%license LICENSE
%{_bindir}/%{name}
