Summary:     Shared library for programs build with p2c Pascal to C convertor
Summary(de): Gemeinsam genutzte Library für Programme, die mit dem Pascal-C-Konverter p2c erstellt wurden
Summary(fr): Librairie partagée pour les programmes construits avec le convertisseur Pascal vers C p2c.
Summary(pl): biblioteka dzielona dla programów skompilowanych po u¿yciu konwertera Pascala do C
Summary(tr): Pascal'dan C'ye çevirici için ortak kitaplýklar
Name:        p2c
Version:     1.20
Release:     11
Copyright:   distributable
Group:       Libraries
Source:      ftp://csvax.cs.caltech.edu/pub/%{name}-%{version}.tar.Z
Patch0:      p2c-misc.patch
Patch1:      p2c-buildroot.patch
Patch2:      p2c-Makefile.patch
BuildRoot:   /tmp/%{name}-%{version}-root

%description
p2c is the Pascal to C translation system.  It is used to convert
Pascal source code into C source code so that it can be compiled
using a standard C compiler (such as gcc).  

%description -l de
p2c ist das Pascal->C-Übersetzungssystem. Es dient zur Konvertierung
von Pascal-Quellcode in C-Quellcode, der dann mit einem Standard-
C-Compiler (etwa gcc) kompiliert werden kann. 

%description -l fr
p2c est le système de traduction Pascal vers C. Il sert à convertir du code
source Pascal en code source C afin qu'il puisse être compilé en utilisant un
compilateur C standard (comme gcc).

%description -l pl
p2c to system t³umaczenia Pascala na C. Konwertuje ¼ród³o w Pascalu na
¼ród³o w C, które mo¿e byæ nastêpnie skompilowane standardowym
kompilatorem C (np. gcc).

%description -l tr
p2c Pascal'dan C'ye çeviricidir. Pascal kodunu C koduna çevirerek sonradan
gcc ya da diðer bir standart C derleyicisi yardýmýyla derlenmesini saðlar.

%package devel
Summary:	programs and header for Pascal to C translator
Summary(de):	Programme und Header für den Pascal-C-Übersetzer
Summary(fr):	Programmes et en-tête pour le convertisseur Pascal vers C.
Summary(pl):	Programy i pliki nag³ówkowe dla translatora Pascala na C
Summary(tr):	Pascal-C çeviricisi için programlar ve baþlýk dosyalarý
Group:		Development/Languages
Requires:	%{name} = %{version}

%description devel
This is the development kit for the Pascal to C translator.
It contains the header files and some other programs that
might be useful to someone using the translator.

%description devel -l de
Dies ist das Entwicklerpaket für de Pascal-C-Übersetzer.
Es enthält die Header-Dateien und Programme, die zum
Einsatz des Übersetzers nützlich sind.

%description devel -l fr
Ceci est le kit de developpement pour le convertisseur Pascal vers C
Il contient les fichiers d'en-tete et d'autres programmes qui peuvent
etre utiles pour utiliser le convertisseur.

%description devel -l pl
Translator Pascala na C. Ten pakiet zawiera program translatora i pliki
nag³ówkowe.

%description devel -l tr
Bu paket, Pascal'dan C'ye çevirici için geliþtirme dosyalarýný içerir.

%package static
Summary:	Pascal to C translator static library
Summary(pl):	Biblioteka statyczna translatora Pascala na C
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Pascal to C translator static library.

%description static -l pl
Biblioteka statyczna translatora Pascala na C.

%package -n basic
Summary:	BASIC interpretor
Summary(de):	BASIC-Interpreter
Summary(fr):	Interpréteur BASIC
Summary(pl):	Interpreter BASICa
Summary(tr):	BASIC yorumlayýcýsý
Group:		Development/Languages

%description -n basic
This is a BASIC language interpreter.  You can use it to run programs
written in BASIC.  For those who may not know, BASIC is an archaic language
used only to learn early fundamentals of programming, and it isn't very good
for that, either. :-)

%description -n basic -l de
Ein Interpretierer für BASIC, den Sie einsetzen können, um BASIC-Programme
auszuführen. Für diejenigen unter Ihnen, die nicht wissen, was BASIC ist: Es
ist eine archaische Sprache, die nur zum Erlernen der frühen Grundlagen der
Programmierung dient, und nicht einmal dafür sonderlich geeignet ist...)

%description -n basic -l fr
Interpréteur BASIC. Utilisé pour exécuter des programmes écrits en BASIC.
Pour ceux qui ne le connaissent pas, BASIC est un langage archaïque
uniquement utilisé pour apprendre les bases de la programmation et, même
pour ça, il n'est pas bon. :-)

%description -n basic -l pl
To jest interpreter BASICa, którym mo¿na uruchamiaæ programy napisane w
BASICu. Je¶li tego nie wiesz, to BASIC jest archaicznym jêzykiem u¿ywanym
tylko do nauki podstaw programowania, ale nawet do tego siê dobrze nie
nadaje :-)

%description -n basic -l tr
Bu paket bir BASIC dili yorumlayýcýsý içerir. BASIC ile yazýlmýþ programlarýn
çalýþtýrýlmasýnda kullanýlýr. Bilmeyenler varsa, BASIC programlamanýn
temellerinin öðrenilmesinde kullanýlan tarih öncesi bir dildir. Aslýnda o
iþe yaradýðý bile söylenemez. :-)

%prep
%setup -c -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
mkdir src/shlib

%build
cp src/sys.p2crc src/p2crc
make
make shlib -C src

%install
rm -rf $RPM_BUILD_ROOT
make install \
	HOMEDIR=$RPM_BUILD_ROOT/usr/lib/p2c \
	INCDIR=$RPM_BUILD_ROOT/usr/include/p2c \
	BINDIR=$RPM_BUILD_ROOT/usr/bin \
	LIBDIR=$RPM_BUILD_ROOT/usr/lib \
	MANDIR=$RPM_BUILD_ROOT/usr/man/man1

install -s examples/basic $RPM_BUILD_ROOT/usr/bin/basic

strip $RPM_BUILD_ROOT/usr/{bin/p2c,lib/lib*.so.*.*}

gzip -9nf $RPM_BUILD_ROOT/usr/man/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644, root, root, 755)
%attr(755, root, root) /usr/bin/p2c
%attr(755, root, root) /usr/lib/lib*.so.*.*
%attr(755, root, root) /usr/lib/p2c
%attr(644, root,  man) /usr/man/man1/*

%files devel
%defattr(644, root, root, 755)
/usr/include/p2c
/usr/lib/lib*.so

%files static
%attr(644, root, root) /usr/lib/lib*.a

%files -n basic
%defattr(644, root, root, 755)
%doc examples/basic.doc
%attr(755, root, root) /usr/bin/basic

%changelog
* Sun Nov 29 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.20-11]
- added gzipping man pages,
- added p2c-Makefile.patch,
- added striping shared libraries.

* Sat Sep 26 1998 Marcin 'Qrczak' Kowalczyk <qrczak@knm.org.pl>
- use %{name} and %{version} macros,
- added %setup -q parameter,
- separated static library subpackage,
- stated that p2c-devel requires p2c, and p2c-static requires p2c-devel,
- added pl translation.

* Tue Aug 18 1998 Cristian Gafton <gafton@redhat.com>
- buildroot
- binary files and man page should really be in the main package, 
  not -devel

* Tue May 05 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
