# TODO: applnk

Summary:	PhpMole is an integrated development enviroment for developing (primarily) web and phpgtk based applications.
Name:		phpmole
Version:	1.3.1
Release:	1
License:	GPL
Group:		X11/Development/Tools
Source0:	http://dl.sourceforge.net/phpmole-ide/%{name}-%{version}.tgz
URL:		http://www.akbkhome.com/Projects/Phpmole-IDE/
Requires:	php-gtk
Requires:	php-dba
Requires:	php-sockets
Requires:	php-curl
Requires:	php-imap
Requires:	php-pecl-imagick
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PhpMole is an integrated development enviroment for developing (primarily) web based
and phpgtk based applications It grew out of porting Moleskine to php when Andrei
(who wrote php- gtk) released bindings for the scintilla widget. Since then it has
got out of control!

In simple words PHPMole is Dreamweaver crossed with MS Visual Studio, with a
Content Mangement interface and Image tools thrown into the bag.....

%prep
%setup -q -n %{name}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

rm -rf phpmole.exe

cp -rf * $RPM_BUILD_ROOT%{_datadir}/%{name}

cat <<EOF > $RPM_BUILD_ROOT%{_bindir}/%{name}
#!/bin/sh
cd %{_datadir}/%{name}
php phpmole-ide.php
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
