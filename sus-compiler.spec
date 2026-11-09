#
# spec file for package sus-compiler
#

Name:           sus-compiler
Version:        0
Release:        0
Summary:        A new Hardware Design Language 

License:        GPL-3.0
Url:            https://github.com/pc2/sus-compiler

Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.zst

Patch2:         0002-do-not-install-sus-libs-to-bin-directory.patch

BuildRequires:  cargo-packaging

%description
A new Hardware Design Language that keeps you in the driver's seat

%package devel
Summary:        sus-compiler development files

%description devel
Those are the development files of sus-compiler

%prep
%autosetup
tar -xf %{_sourcedir}/vendor.tar.zst --directory .

%build

# Imitate rust's vergen git variable
export VERGEN_GIT_DESCRIBE=v%{version}
export SUS_COMPILER_STD_LIB_PATH=%{_datadir}/sus_compiler/stl

%{cargo_build}

%install
export SUS_COMPILER_STD_LIB_PATH=%{_datadir}/sus_compiler/stl
%{cargo_install}

install -D -t "%{buildroot}%{_datadir}/sus_compiler/stl/" stl/*

%check
export SUS_COMPILER_STD_LIB_PATH=%{_datadir}/sus_compiler/stl
%{cargo_test}

%files
%{_bindir}/sus_compiler

%dir %{_datadir}/sus_compiler
%dir %{_datadir}/sus_compiler/stl
%{_datadir}/sus_compiler/stl/*

%license LICENSE
%doc README.md

%changelog
