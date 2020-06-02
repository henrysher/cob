%define pluginhome /usr/lib/yum-plugins

%global provider        github
%global provider_tld    com
%global project         henrysher
%global repo            cob
# https://github.com/henrysher/cob
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global commit          1e5e1f25d843a9ae676abdd015fcf3459cefe869
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           yum-plugin-cob
Version:        0.3.1
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        Yet Another Yum S3 Plugin (AWS SigV4)
License:        ASL 2.0
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz

BuildArch:      noarch

Requires:       yum

# handle license on el{6,7}: global must be defined after the License field above
%{!?_licensedir: %global license %doc}

%description
Cob, yet another yum S3 plugin, provides the way to accessing yum repository hosted on AWS S3.

%prep
%setup -q -n %{repo}-%{commit}

%build

%install
make DESTDIR=$RPM_BUILD_ROOT install

mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/yum/pluginconf.d/ $RPM_BUILD_ROOT/%pluginhome
install -m 644 %{repo}.conf $RPM_BUILD_ROOT/%{_sysconfdir}/yum/pluginconf.d/
install -m 644 %{repo}.py $RPM_BUILD_ROOT/%pluginhome

%files
%doc %{repo}.repo README.md
%license LICENSE
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/%{repo}.conf
%pluginhome/%{repo}.py*

%changelog
* Wed Oct 25 2017 Marcin Dulak <Marcin.Dulak@gmail.com> 0.3.1-0.1.git1e5e1f2
- Initial fedora package
