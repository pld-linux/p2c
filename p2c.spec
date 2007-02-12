Summary:	Shared library for programs build with p2c Pascal to C convertor
Summary(de.UTF-8):   Gemeinsam genutzte Library für Programme, die mit dem Pascal-C-Konverter p2c erstellt wurden
Summary(es.UTF-8):   Biblioteca compartida para programas hechos con el convertidor p2c de pascal a C
Summary(fr.UTF-8):   Librairie partagée pour les programmes construits avec le convertisseur Pascal vers C p2c
Summary(pl.UTF-8):   Biblioteka dzielona dla programów skompilowanych po użyciu konwertera Pascala do C
Summary(pt_BR.UTF-8):   Biblioteca compartilhada para programas feitos com o conversor p2c de pascal para C
Summary(ru.UTF-8):   Конвертор из Pascal в C
Summary(tr.UTF-8):   Pascal'dan C'ye çevirici için ortak kitaplıklar
Summary(uk.UTF-8):   Конвертор з Pascal в C
Name:		p2c
Version:	1.22
Release:	14
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

%description -l de.UTF-8
p2c ist das Pascal->C-Übersetzungssystem. Es dient zur Konvertierung
von Pascal-Quellcode in C-Quellcode, der dann mit einem Standard-
C-Compiler (etwa gcc) kompiliert werden kann.

%description -l es.UTF-8
p2c es un traductor de Pascal para C. Se usa para convertir el código
fuente Pascal en código fuente C, éste puede ser compilado usándose un
compilador C padrón (como gcc).

%description -l fr.UTF-8
p2c est le système de traduction Pascal vers C. Il sert à convertir du
code source Pascal en code source C afin qu'il puisse être compilé en
utilisant un compilateur C standard (comme gcc).

%description -l pl.UTF-8
p2c to system tłumaczenia Pascala na C. Konwertuje źródło w Pascalu na
źródło w C, które może być następnie skompilowane standardowym
kompilatorem C (np. gcc).

%description -l pt_BR.UTF-8
O p2c é um tradutor de Pascal para C. Ele é usado para converter o
código fonte Pascal em código fonte C, então este pode ser compilado
usando-se um compilador C padrão (como gcc).

%description -l ru.UTF-8
p2c - это транслятор из Pascal в C. Он используется для трансляции
исходных текстов на Pascal в исходные тексты на C, которые могут быть
откомпиллированы стандартным компиллятором C (например, gcc).

%description -l tr.UTF-8
p2c Pascal'dan C'ye çeviricidir. Pascal kodunu C koduna çevirerek
sonradan gcc ya da diğer bir standart C derleyicisi yardımıyla
derlenmesini sağlar.

%description -l uk.UTF-8
p2c - це транслятор з Pascal в C. Він використовується для трансляції
вихідних текстів на Pascal у вихідні тексти на C, які можуть бути
відкомпільовані стандартним компилятором C (наприклад, gcc).

%package devel
Summary:	Programs and header for Pascal to C translator
Summary(de.UTF-8):   Programme und Header für den Pascal-C-Übersetzer
Summary(es.UTF-8):   Programas y archivos de inclusión para el traductor de Pascal a C
Summary(fr.UTF-8):   Programmes et en-tête pour le convertisseur Pascal vers C
Summary(pl.UTF-8):   Programy i pliki nagłówkowe dla translatora Pascala na C
Summary(pt_BR.UTF-8):   Programas e arquivos de inclusão para o tradutor de Pascal para C
Summary(ru.UTF-8):   Файлы для разработки p2c, транслятора из Pascal в C
Summary(tr.UTF-8):   Pascal-C çeviricisi için programlar ve başlık dosyaları
Summary(uk.UTF-8):   Файли для розробки p2c, транслятора з Pascal в C
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description devel
This is the development kit for the Pascal to C translator. It
contains the header files and some other programs that might be useful
to someone using the translator.

%description devel -l de.UTF-8
Dies ist das Entwicklerpaket für de Pascal-C-Übersetzer. Es enthält
die Header-Dateien und Programme, die zum Einsatz des Übersetzers
nützlich sind.

%description devel -l es.UTF-8
Este es el kit de desarrollo para el traductor de Pascal para C.
Contiene los archivos de inclusión y algunos programas que pueden ser
útiles para quien usa el traductor.

%description devel -l fr.UTF-8
Ceci est le kit de developpement pour le convertisseur Pascal vers C
Il contient les fichiers d'en-tete et d'autres programmes qui peuvent
etre utiles pour utiliser le convertisseur.

%description devel -l pl.UTF-8
Translator Pascala na C. Ten pakiet zawiera program translatora i
pliki nagłówkowe.

%description devel -l pt_BR.UTF-8
Este é o kit de desenvolvimento para o tradutor de Pascal para C.
Contém os arquivos de inclusão e alguns programas que podem ser úteis
para quem usa o tradutor.

%description devel -l ru.UTF-8
Пакет p2c-devel содержит файлы, необходимые для разработки транслятора
из Pascal в C, p2c.

%description devel -l tr.UTF-8
Bu paket, Pascal'dan C'ye çevirici için geliştirme dosyalarını içerir.

%description devel -l uk.UTF-8
Пакет p2c-devel містить файли, необхідні для розробки транслятора з
Pascal в C, p2c.

%package static
Summary:	Pascal to C translator static library
Summary(pl.UTF-8):   Biblioteka statyczna translatora Pascala na C
Summary(pt_BR.UTF-8):   Bibliotecas estáticas para desenvolvimento com p2c
Summary(ru.UTF-8):   Статические библиотеки для разработки p2c, транслятора из Pascal в C
Summary(uk.UTF-8):   Статичні бібліотеки для розробки p2c, транслятора з Pascal в C
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Pascal to C translator static library.

%description static -l pl.UTF-8
Biblioteka statyczna translatora Pascala na C.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento com p2c.

%description static -l ru.UTF-8
Пакет p2c-devel содержит статические библиотеки, необходимые для
разработки транслятора из Pascal в C, p2c.

%description static -l uk.UTF-8
Пакет p2c-devel містить статичні бібліотеки, необхідні для розробки
транслятора з Pascal в C, p2c.

%package -n basic
Summary:	BASIC interpretor
Summary(de.UTF-8):   BASIC-Interpreter
Summary(fr.UTF-8):   Interpréteur BASIC
Summary(pl.UTF-8):   Interpreter BASICa
Summary(tr.UTF-8):   BASIC yorumlayıcısı
Group:		Development/Languages

%description -n basic
This is a BASIC language interpreter. You can use it to run programs
written in BASIC. For those who may not know, BASIC is an archaic
language used only to learn early fundamentals of programming, and it
isn't very good for that, either. :-)

%description -n basic -l de.UTF-8
Ein Interpretierer für BASIC, den Sie einsetzen können, um
BASIC-Programme auszuführen. Für diejenigen unter Ihnen, die nicht
wissen, was BASIC ist: Es ist eine archaische Sprache, die nur zum
Erlernen der frühen Grundlagen der Programmierung dient, und nicht
einmal dafür sonderlich geeignet ist...)

%description -n basic -l fr.UTF-8
Interpréteur BASIC. Utilisé pour exécuter des programmes écrits en
BASIC. Pour ceux qui ne le connaissent pas, BASIC est un langage
archaïque uniquement utilisé pour apprendre les bases de la
programmation et, même pour ça, il n'est pas bon. :-)

%description -n basic -l pl.UTF-8
To jest interpreter BASICa, którym można uruchamiać programy napisane
w BASICu. Jeśli tego nie wiesz, to BASIC jest archaicznym językiem
używanym tylko do nauki podstaw programowania, ale nawet do tego się
dobrze nie nadaje :-)

%description -n basic -l tr.UTF-8
Bu paket bir BASIC dili yorumlayıcısı içerir. BASIC ile yazılmış
programların çalıştırılmasında kullanılır. Bilmeyenler varsa, BASIC
programlamanın temellerinin öğrenilmesinde kullanılan tarih öncesi bir
dildir. Aslında o işe yaradığı bile söylenemez. :-)

%prep
%setup -q
%patch0 -p1
%patch1 -p1
install -d src/shlib include
ln -sf ../src include/p2c

%build
cp -f src/sys.p2crc src/p2crc
%{__make} \
	RPM_OPTS="%{rpmcflags} -fPIC" \
	LIBDIR="%{_libdir}" \
	ABSHOMEDIR="%{_libdir}/p2c" \
	HOMEDIR="%{_libdir}/p2c"

ln -sf src p2c
%{__make} -C examples basic \
	RPM_OPTS="%{rpmcflags} -fPIC -I.." \
	LIBDIR="%{_libdir}" \
	ABSHOMEDIR="%{_libdir}/p2c" \
	HOMEDIR="$RPM_BUILD_ROOT%{_libdir}/p2c"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_mandir}/man1,%{_includedir},%{_bindir}}

%{__make} install \
	RPM_INSTALL=$RPM_BUILD_ROOT \
	LIBDIR="$RPM_BUILD_ROOT%{_libdir}" \
	ABSHOMEDIR="%{_libdir}/p2c" \
	HOMEDIR="$RPM_BUILD_ROOT%{_libdir}/p2c"

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
