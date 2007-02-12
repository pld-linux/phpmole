# TODO: applnk
Summary:	PhpMole - integrated development enviroment for web and PHP-GTK based applications
Summary(pl.UTF-8):   PhpMole - zintegrowane środowisko programisty do applikacji WWW i opartych o PHP-GTK
Name:		phpmole
Version:	1.3.1
Release:	1
License:	GPL
Group:		X11/Development/Tools
Source0:	http://dl.sourceforge.net/phpmole-ide/%{name}-%{version}.tgz
# Source0-md5:	e8b80562fcd718f6f0e54baf5c5744f1
URL:		http://www.akbkhome.com/Projects/Phpmole-IDE/
Requires:	php4-cli
Requires:	php4-curl
Requires:	php4-dba
Requires:	php4-gtk
Requires:	php4-imap
Requires:	php4-pecl-imagick
Requires:	php4-sockets
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PhpMole is an integrated development enviroment for developing
(primarily) web based and PHP-GTK based applications. It grew out of
porting Moleskine to PHP when Andrei (who wrote PHP-GTK) released
bindings for the scintilla widget. Since then it has got out of
control!

In simple words PHPMole is Dreamweaver crossed with MS Visual Studio,
with a Content Mangement interface and Image tools thrown into the
bag...

%description -l pl.UTF-8
PhpMole jest zintegrowanym środowiskiem programisty (IDE) służącym
(przede wszystkim) do tworzenia aplikacji WWW i opartych o PHP-GTK.
Powstał on w wyniku migracji Moleskine do PHP dokonanej, gdy Andrei
(który napisał PHP-GTK) wypuścił sterownik do kontrolki scintilla. W
tamtym momencie wymknął się on spod kontroli!

Prostymi słowami, PHPMole stanowi skrzyżowanie Dreamweavera i MS
Visual Studio z dorzuconymi: interfejsem "Content Mangement" i
narzędziami do obrazków...

%prep
%setup -q -n %{name}

rm -f phpmole.exe

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}

cp -rf * $RPM_BUILD_ROOT%{_datadir}/%{name}

cat <<EOF > $RPM_BUILD_ROOT%{_bindir}/%{name}
#!/bin/sh
cd %{_datadir}/%{name}
exec /usr/bin/php4.cli phpmole-ide.php
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
