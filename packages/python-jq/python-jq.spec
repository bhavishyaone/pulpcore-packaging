%global debug_package %{nil}

%global __python3 /usr/bin/python3.11
%global python3_pkgversion 3.11


# Created by pyp2rpm-3.3.8
%global pypi_name jq

Name:           python-%{pypi_name}
Version:        1.8.0
Release:        1%{?dist}
Summary:        jq is a lightweight and flexible JSON processor

License:        BSD 2-Clause
URL:            https://github.com/mwilliamson/jq.py
Source0:        https://files.pythonhosted.org/packages/source/j/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools


%description
%{summary}


%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}


%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
set -ex
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
set -ex
%py3_build


%install
set -ex
%py3_install


%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%{python3_sitearch}/%{pypi_name}%{python3_ext_suffix}


%changelog
* Thu Oct 03 2024 Foreman Packaging Automation <packaging@theforeman.org> - 1.8.0-1
- Update to 1.8.0

* Tue Jan 16 2024 Odilon Sousa <osousa@redhat.com> - 1.6.0-4
- Remove SCL bits

* Tue Dec 12 2023 Patrick Creech <pcreech@redhat.com> - 1.6.0-3
- Rollback overzealous obsoletes

* Tue Nov 21 2023 Patrick Creech <pcreech@redhat.com> - 1.6.0-2
- Add python39 obsoletes to package

* Mon Nov 13 2023 Odilon Sousa <osousa@redhat.com> - 1.6.0-1
- Initial package.
