# revision 23089
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-tcdialog
Version:	20111104
Release:	6
Summary:	TeXLive tcdialog package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tcdialog.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tcdialog.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Provides:	texlive-tcdialog.bin = %{EVRD}
Requires:	cdialog

%description
TeXLive tcdialog package.

#-----------------------------------------------------------------------
%files
%{_bindir}/tcdialog
%doc %{_mandir}/man1/tcdialog.1*
%doc %{_texmfdir}/doc/man/man1/tcdialog.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf cdialog tcdialog
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111104-2
+ Revision: 756514
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111104-1
+ Revision: 719658
- texlive-tcdialog
- texlive-tcdialog
- texlive-tcdialog
- texlive-tcdialog

