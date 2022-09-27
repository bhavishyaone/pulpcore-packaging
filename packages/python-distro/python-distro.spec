%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-3.3.7
%global pypi_name distro
%global pypi_version 1.7.0

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Distro - an OS platform information API

License:        Apache License, Version 2.0
URL:            https://github.com/python-distro/distro
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

Requires:       %{?scl_prefix}python%{python3_pkgversion}-setuptools

%description -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%autosetup -n %{pypi_name}-%{pypi_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
%{?scl:EOF}


%build
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%py3_build
%{?scl:EOF}


%install
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%py3_install
%{?scl:EOF}


%files -n %{?scl_prefix}python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.md
%exclude %{_bindir}/distro
%{python3_sitelib}/distro/__pycache__/*
%{python3_sitelib}/distro/*.py
%{python3_sitelib}/distro/py.typed
%{python3_sitelib}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info


%changelog
* Tue Sep 27 2022 Odilon Sousa <osousa@redhat.com> - 1.7.0-1
- Release python-distro 1.7.0

* Fri Apr 22 2022 Yanis Guenane <yguenane@redhat.com> - 1.6.0-3
- Build against python 3.9

* Fri Jan 28 2022 Evgeni Golov - 1.6.0-2
- don't include binary to avoid conflicts

* Fri Sep 10 2021 Evgeni Golov - 1.6.0-1
- Initial package.
