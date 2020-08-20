%{?nodejs_find_provides_and_requires}
%global enable_tests 1
Name:                nodejs-glob
Version:             6.0.4
Release:             1
Summary:             A little globber for Node.js
License:             BSD
URL:                 https://github.com/isaacs/node-glob
Source0:             https://github.com/isaacs/node-glob/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:              nodejs-glob-tap.patch
BuildArch:           noarch
ExclusiveArch:       %{nodejs_arches} noarch
BuildRequires:       nodejs-packaging
%if 0%{?enable_tests}
BuildRequires:       npm(tap) npm(inflight) npm(path-is-absolute) npm(rimraf)
%endif
%description
This is a glob implementation in pure JavaScript. It uses the minimatch library
to do its matching.

%prep
%autosetup -p 1 -n node-glob-%{version}
%nodejs_fixdep once "^1.1.1"

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/glob
cp -pr package.json glob.js sync.js common.js \
  %{buildroot}%{nodejs_sitelib}/glob
%nodejs_symlink_deps
%if 0%{?enable_tests}

%check
%nodejs_symlink_deps --check
%tap test/*.js
%endif

%files
%{!?_licensedir:%global license %doc}
%doc README.md examples
%license LICENSE
%{nodejs_sitelib}/glob

%changelog
* Thu Aug 20 2020 Anan Fu <fuanan3@huawei.com> - 6.0.4-1
- package init
