# revision 23089
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-tcdialog
Version:	20111104
Release:	1
Summary:	TeXLive tcdialog package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tcdialog.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tcdialog.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Provides:	texlive-tcdialog.bin = %{EVRD}
Requires:	cdialog
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
TeXLive tcdialog package.

#-----------------------------------------------------------------------
%files
%{_bindir}/tcdialog
%doc %{_mandir}/man1/tcdialog.1*
%doc %{_texmfdir}/doc/man/man1/tcdialog.man1.pdf
%doc %{_tlpkgobjdir}/*.tlpobj

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
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
