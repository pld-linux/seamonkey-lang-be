Summary:	Belarusian resources for SeaMonkey
Summary(pl):	Bia³oruskie pliki jêzykowe dla SeaMonkeya
Name:		seamonkey-lang-be
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/contrib-localized/seamonkey-%{version}.be-BY.langpack.xpi
# Source0-md5:	ffb6a2f2ba0a6d2aefde3d8a13f272ee
Source1:	gen-installed-chrome.sh
URL:		http://www.mozilla.org/projects/seamonkey/
BuildRequires:	unzip
Requires(post,postun):	seamonkey >= %{version}
Requires(post,postun):	textutils
Requires:	seamonkey >= %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_chromedir	%{_datadir}/seamonkey/chrome

%description
Belarusuian resources for SeaMonkey.

%description -l pl
Bia³oruskie pliki jêzykowe dla SeaMonkeya.

%prep
%setup -q -c
install %{SOURCE1} .
./gen-installed-chrome.sh locale bin/chrome/{BY,be-BY,be-unix}.jar \
	> lang-be-installed-chrome.txt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

install bin/chrome/{BY,be-BY,be-unix}.jar $RPM_BUILD_ROOT%{_chromedir}
install lang-be-installed-chrome.txt $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/seamonkey-chrome+xpcom-generate

%postun
%{_sbindir}/seamonkey-chrome+xpcom-generate

%files
%defattr(644,root,root,755)
%{_chromedir}/BY.jar
%{_chromedir}/be-BY.jar
%{_chromedir}/be-unix.jar
%{_chromedir}/lang-be-installed-chrome.txt
