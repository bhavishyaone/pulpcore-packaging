Name: pulpcore-obsolete-packages
Version: 1.0
Release: 8%{?dist}
License: MIT
Summary: A package to obsolete retired packages
URL: https://github.com/theforeman/pulpcore-packaging
BuildArch: noarch

Obsoletes:      python3-django-currentuser < 0.5.3-6
%if 0%{?rhel} == 8
Obsoletes:      python39-django-currentuser < 0.5.3-6
Obsoletes:      python39-importlib-resources < 5.4.0-6
Obsoletes:      python39-django-guardian < 2.4.0-7
Obsoletes:      python39-aiodns < 3.0.0-4
Obsoletes:      python39-aiohttp < 3.8.3-3
Obsoletes:      python39-aiohttp-xmlrpc < 1.5.0-3
Obsoletes:      python39-pexpect < 4.8.0-3
Obsoletes:      python39-requests < 2.31.0-2
Obsoletes:      python39-wcmatch < 8.3-3
Obsoletes:      python39-aiohttp-socks < 0.7.1-4
Obsoletes:      python39-pypi-simple < 0.9.0-3
%endif

%description
This package exists only to obsolete other packages which need to be removed
from the distribution for some reason.

%prep

%build

%install

%files

%changelog
* Thu Jan 11 2024 Patrick Creech <pcreech@redhat.com> - 1.0-8
- Obsolete aiohttp-socks and pypi-simple as well

* Wed Jan 10 2024 Patrick Creech <pcreech@redhat.com> - 1.0-7
- Obsolete packages to ensure consistent upgrads in older systems

* Thu Dec 14 2023 Odilon Sousa <osousa@redhat.com> - 1.0-6
- Dont obsolete pyyaml

* Fri Dec 08 2023 Patrick Creech <pcreech@redhat.com> - 1.0-5
- Add django-guardian and importlib-resources to obsoletes

* Wed Nov 22 2023 Patrick Creech <pcreech@redhat.com> - 1.0-4
- Don't obsolete python3-pyyaml

* Wed Nov 22 2023 Patrick Creech <pcreech@redhat.com> - 1.0-3
- Obsolete the python39 pyyaml, as ansible brings in a pyyaml newer than the one we provide

* Mon Aug 28 2023 Odilon Sousa <osousa@redhat.com> - 1.0-2
- Pin the version of django-currentuser

* Tue Aug 15 2023 Zach Huntington-Meath <zhunting@redhat.com> - 1.0-1
- Initial package
