%{?python_disable_dependency_generator}
%global pypi_name opentelemetry_exporter_otlp_proto_grpc

Name:           python-%{pypi_name}
Version:        1.19.0
Release:        1%{?dist}
Summary:        OpenTelemetry Collector Protobuf over gRPC Exporter

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-python/tree/main/exporter/opentelemetry-exporter-otlp-proto-grpc
Source:         https://files.pythonhosted.org/packages/source/o/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-hatchling
BuildRequires:  python%{python3_pkgversion}-tomli

%description
%{summary}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
Requires:       python%{python3_pkgversion}-deprecated >= 1.2.6
Requires:       python%{python3_pkgversion}-backoff >= 1.10.0
Requires:       python%{python3_pkgversion}-backoff <  3.0.0
Requires:       python%{python3_pkgversion}-googleapis-common-protos >= 1.52
Requires:       python%{python3_pkgversion}-googleapis-common-protos >= 2
Requires:       python%{python3_pkgversion}-grpcio >= 1.0.0
Requires:       python%{python3_pkgversion}-grpcio < 2.0.0
Requires:       python%{python3_pkgversion}-opentelemetry-api >= 1.15.0
Requires:       python%{python3_pkgversion}-opentelemetry-api < 2.0.0
Requires:       python%{python3_pkgversion}-opentelemetry-proto = 1.19.0
Requires:       python%{python3_pkgversion}-opentelemetry-sdk  >= 1.19.0
Requires:       python%{python3_pkgversion}-opentelemetry-sdk  < 2.0.0
Requires:       python%{python3_pkgversion}-opentelemetry-exporter-otlp-proto-common = 1.19.0


%description -n python%{python3_pkgversion}-%{pypi_name}
%{summary}


%prep
set -ex
%autosetup -n %{pypi_name}-%{version}


%build
set -ex
%pyproject_wheel


%install
set -ex
%pyproject_install

%files -n python%{python3_pkgversion}-%{pypi_name}
%{python3_sitelib}/opentelemetry/exporter/otlp/proto/grpc/
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/


%changelog
* Wed Jul 26 2023 Odilon Sousa - 1.19.0-1
- Initial package.