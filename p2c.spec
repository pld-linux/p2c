Summary:	Shared library for programs build with p2c Pascal to C convertor
Summary(de):	Gemeinsam genutzte Library fЭr Programme, die mit dem Pascal-C-Konverter p2c erstellt wurden
Summary(es):	Biblioteca compartida para programas hechos con el convertidor p2c de pascal a C
Summary(fr):	Librairie partagИe pour les programmes construits avec le convertisseur Pascal vers C p2c
Summary(pl):	Biblioteka dzielona dla programСw skompilowanych po u©yciu konwertera Pascala do C
Summary(pt_BR):	Biblioteca compartilhada para programas feitos com o conversor p2c de pascal para C
Summary(ru):	Конвертор из Pascal в C
Summary(tr):	Pascal'dan C'ye Гevirici iГin ortak kitaplЩklar
Summary(uk):	Конвертор з Pascal в C
Name:		p2c
Version:	1.22
Release:	12
License:	distributable
Group:		Libraries
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	78eca593810d037bf5631d934168fe0d
Patch0:		%{name}-makefiles.patch
Patch1:		%{name}-dos.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
p2c is the Pascal to C translation system. It is used to convert
Pascal source code into C source code so that it can be compiled using
a standard C compiler (such as gcc).

%description -l de
p2c ist das Pascal->C-эbersetzungssystem. Es dient zur Konvertierung
von Pascal-Quellcode in C-Quellcode, der dann mit einem Standard-
C-Compiler (etwa gcc) kompiliert werden kann.

%description -l es
p2c es un traductor de Pascal para C. Se usa para convertir el
cСdigo fuente Pascal en cСdigo fuente C, Иste puede ser compilado
usАndose un compilador C padrСn (como gcc).

%description -l fr
p2c est le systХme de traduction Pascal vers C. Il sert Ю convertir du
code source Pascal en code source C afin qu'il puisse Йtre compilИ en
utilisant un compilateur C standard (comme gcc).

%description -l pl
p2c to system tЁumaczenia Pascala na C. Konwertuje ╪rСdЁo w Pascalu na
╪rСdЁo w C, ktСre mo©e byФ nastЙpnie skompilowane standardowym
kompilatorem C (np. gcc).

%description -l pt_BR
O p2c И um tradutor de Pascal para C. Ele И usado para converter o
cСdigo fonte Pascal em cСdigo fonte C, entЦo este pode ser compilado
usando-se um compilador C padrЦo (como gcc).
 
%description -l ru
p2c - это транслятор из Pascal в C. Он используется для трансляции
исходных текстов на Pascal в исходные тексты на C, которые могут
быть откомпиллированы стандартным компиллятором C (например, gcc).

%description -l tr
p2c Pascal'dan C'ye Гeviricidir. Pascal kodunu C koduna Гevirerek
sonradan gcc ya da diПer bir standart C derleyicisi yardЩmЩyla
derlenmesini saПlar.

%description -l uk
p2c - це транслятор з Pascal в C. В╕н використову╓ться для трансляц╕╖
вих╕дних текст╕в на Pascal у вих╕дн╕ тексти на C, як╕ можуть бути
в╕дкомп╕льован╕ стандартним компилятором C (наприклад, gcc).

%package devel
Summary:	programs and header for Pascal to C translator
Summary(de):	Programme und Header fЭr den Pascal-C-эbersetzer
Summary(es):	Programas y archivos de inclusiСn para el traductor de Pascal a C
Summary(fr):	Programmes et en-tЙte pour le convertisseur Pascal vers C
Summary(pl):	Programy i pliki nagЁСwkowe dla translatora Pascala na C
Summary(pt_BR):	Programas e arquivos de inclusЦo para o tradutor de Pascal para C
Summary(ru):	Файлы для разработки p2c, транслятора из Pascal в C
Summary(tr):	Pascal-C Гeviricisi iГin programlar ve baЧlЩk dosyalarЩ
Summary(uk):	Файли для розробки p2c, транслятора з Pascal в C
Group:		Development/Languages
Requires:	%{name} = %{version}

%description devel
This is the development kit for the Pascal to C translator. It
contains the header files and some other programs that might be useful
to someone using the translator.

%description devel -l de
Dies ist das Entwicklerpaket fЭr de Pascal-C-эbersetzer. Es enthДlt
die Header-Dateien und Programme, die zum Einsatz des эbersetzers
nЭtzlich sind.

%description devel -l es
Este es el kit de desarrollo para el traductor de Pascal para C.
Contiene los archivos de inclusiСn y algunos programas que pueden
ser Зtiles para quien usa el traductor.

%description devel -l fr
Ceci est le kit de developpement pour le convertisseur Pascal vers C
Il contient les fichiers d'en-tete et d'autres programmes qui peuvent
etre utiles pour utiliser le convertisseur.

%description devel -l pl
Translator Pascala na C. Ten pakiet zawiera program translatora i
pliki nagЁСwkowe.

%description devel -l pt_BR
Este И o kit de desenvolvimento para o tradutor de Pascal para C.
ContИm os arquivos de inclusЦo e alguns programas que podem ser Зteis
para quem usa o tradutor.

%description devel -l ru
Пакет p2c-devel содержит файлы, необходимые для разработки транслятора
из Pascal в C, p2c.

%description devel -l tr
Bu paket, Pascal'dan C'ye Гevirici iГin geliЧtirme dosyalarЩnЩ iГerir.

%description devel -l uk
Пакет p2c-devel м╕стить файли, необх╕дн╕ для розробки транслятора
з Pascal в C, p2c.

%package static
Summary:	Pascal to C translator static library
Summary(pl):	Biblioteka statyczna translatora Pascala na C
Summary(pt_BR):	Bibliotecas estАticas para desenvolvimento com p2c
Summary(ru):	Статические библиотеки для разработки p2c, транслятора из Pascal в C
Summary(uk):	Статичн╕ б╕бл╕отеки для розробки p2c, транслятора з Pascal в C
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Pascal to C translator static library.

%description static -l pl
Biblioteka statyczna translatora Pascala na C.

%description static -l pt_BR
Bibliotecas estАticas para desenvolvimento com p2c.

%description static -l ru
Пакет p2c-devel содержит статические библиотеки, необходимые для разработки
транслятора из Pascal в C, p2c.

%description static -l uk
Пакет p2c-devel м╕стить статичн╕ б╕бл╕отеки, необх╕дн╕ для розробки
транслятора з Pascal в C, p2c.
 
%package -n basic
Summary:	BASIC interpretor
Summary(de):	BASIC-Interpreter
Summary(fr):	InterprИteur BASIC
Summary(pl):	Interpreter BASICa
Summary(tr):	BASIC yorumlayЩcЩsЩ
Group:		Development/Languages

%description -n basic
This is a BASIC language interpreter. You can use it to run programs
written in BASIC. For those who may not know, BASIC is an archaic
language used only to learn early fundamentals of programming, and it
isn't very good for that, either. :-)

%description -n basic -l de
Ein Interpretierer fЭr BASIC, den Sie einsetzen kЖnnen, um
BASIC-Programme auszufЭhren. FЭr diejenigen unter Ihnen, die nicht
wissen, was BASIC ist: Es ist eine archaische Sprache, die nur zum
Erlernen der frЭhen Grundlagen der Programmierung dient, und nicht
einmal dafЭr sonderlich geeignet ist...)

%description -n basic -l fr
InterprИteur BASIC. UtilisИ pour exИcuter des programmes Иcrits en
BASIC. Pour ceux qui ne le connaissent pas, BASIC est un langage
archaОque uniquement utilisИ pour apprendre les bases de la
programmation et, mЙme pour Гa, il n'est pas bon. :-)

%description -n basic -l pl
To jest interpreter BASICa, ktСrym mo©na uruchamiaФ programy napisane
w BASICu. Je╤li tego nie wiesz, to BASIC jest archaicznym jЙzykiem
u©ywanym tylko do nauki podstaw programowania, ale nawet do tego siЙ
dobrze nie nadaje :-)

%description -n basic -l tr
Bu paket bir BASIC dili yorumlayЩcЩsЩ iГerir. BASIC ile yazЩlmЩЧ
programlarЩn ГalЩЧtЩrЩlmasЩnda kullanЩlЩr. Bilmeyenler varsa, BASIC
programlamanЩn temellerinin ЖПrenilmesinde kullanЩlan tarih Жncesi bir
dildir. AslЩnda o iЧe yaradЩПЩ bile sЖylenemez. :-)

%prep
%setup -q
%patch0 -p1
%patch1 -p1
install -d src/shlib include
ln -sf ../src include/p2c

%build
cp -f src/sys.p2crc src/p2crc
%{__make} RPM_OPTS="%{rpmcflags}"
ln -sf src p2c
%{__make} RPM_OPTS="%{rpmcflags} -I.." basic -C examples

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_mandir}/man1,%{_includedir},%{_bindir}}

%{__make} install RPM_INSTALL=$RPM_BUILD_ROOT

ln -sf libp2c.so.1.2.0 $RPM_BUILD_ROOT%{_libdir}/libp2c.so
install examples/basic $RPM_BUILD_ROOT%{_bindir}/basic

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/p2c*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_libdir}/p2c
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%doc ChangeLog README src/{HISTORY,NOTES}
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/p2c

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files -n basic
%defattr(644,root,root,755)
%doc examples/basic.doc
%attr(755,root,root) %{_bindir}/basic
