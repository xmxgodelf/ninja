Summary: Ninja is a small build system with a focus on speed.
Name: ninja-build
Version: %{ver}
Release: zy_1.0.0_1.ctyunos
Group: Development/Tools
License: Apache 2.0
URL: https://github.com/ninja-build/ninja
Source0: %{name}-%{version}-%{rel}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{rel}

BuildRequires: asciidoc

%description
Ninja is yet another build system. It takes as input the interdependencies of files (typically source code and output executables) and
orchestrates building them, quickly.

Ninja joins a sea of other build systems. Its distinguishing goal is to be fast. It is born from my work on the Chromium browser project,
which has over 30,000 source files and whose other build systems (including one built from custom non-recursive Makefiles) can take ten
seconds to start building after changing one file. Ninja is under a second.

%prep
%setup -q -n %{name}-%{version}-%{rel}

%build
echo Building..
./configure.py --bootstrap
./ninja -v manual
./ninja -v ninja_test

%install
install -Dpm0755 ninja %{buildroot}%{_bindir}/ninja
install -Dpm0644 misc/bash-completion %{buildroot}%{_datadir}/bash-completion/completions/ninja
install -Dpm0644 misc/ninja-mode.el %{buildroot}%{_datadir}/emacs/site-lisp/ninja-mode.el
install -Dpm0644 misc/ninja.vim %{buildroot}%{_datadir}/vim/vimfiles/syntax/ninja.vim
install -Dpm0644 misc/ninja.vim %{buildroot}%{_datadir}/vim/vimfiles/ftdetect/ninja.vim
install -Dpm0644 misc/macros.ninja %{buildroot}%{rpmmacrodir}/macros.ninja
install -Dpm0644 misc/zsh-completion %{buildroot}%{_datadir}/zsh/site-functions/_ninja
ln -s ninja %{buildroot}%{_bindir}/ninja-build


%files
%defattr(-, root, root)
%doc COPYING README.md doc/manual.html
%{_bindir}/*
%{rpmmacrodir}/*

%clean
rm -rf %{buildroot}

#The changelog is built automatically from Git history
%changelog
