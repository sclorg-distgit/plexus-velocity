%global pkg_name plexus-velocity
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

# Copyright (c) 2000-2005, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

%define parent plexus
%define subname velocity

Name:           %{?scl_prefix}%{pkg_name}
Version:        1.1.8
Release:        16.10%{?dist}
Epoch:          0
Summary:        Plexus Velocity Component
License:        ASL 2.0
URL:            http://plexus.codehaus.org/
# svn export http://svn.codehaus.org/plexus/plexus-components/tags/plexus-velocity-1.1.8/
# tar czf plexus-velocity-1.1.8-src.tar.gz plexus-velocity-1.1.8/
Source0:        plexus-velocity-%{version}-src.tar.gz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

BuildArch:      noarch
BuildRequires:  %{?scl_prefix_java_common}javapackages-tools
BuildRequires:  %{?scl_prefix_java_common}ant >= 0:1.6
BuildRequires:  %{?scl_prefix_java_common}maven-local
BuildRequires:  %{?scl_prefix}maven-resources-plugin
BuildRequires:  %{?scl_prefix}maven-doxia-sitetools
BuildRequires:  %{?scl_prefix}ant-contrib
BuildRequires:  %{?scl_prefix}plexus-classworlds >= 0:1.1
BuildRequires:  %{?scl_prefix_java_common}apache-commons-collections
BuildRequires:  %{?scl_prefix}plexus-containers-container-default
BuildRequires:  %{?scl_prefix}plexus-utils
BuildRequires:  %{?scl_prefix}velocity

%description
The Plexus project seeks to create end-to-end developer tools for
writing applications. At the core is the container, which can be
embedded or for a full scale application server. There are many
reusable components for hibernate, form processing, jndi, i18n,
velocity, etc. Plexus also includes an application server which
is like a J2EE application server, without all the baggage.

%package javadoc
Summary:        Javadoc for %{pkg_name}

%description javadoc
Javadoc for %{pkg_name}.

%prep
%setup -q -n plexus-velocity-%{version}
%{?scl:scl enable %{scl_java_common} %{scl_maven} %{scl} - <<"EOF"}
set -e -x
cp -p %{SOURCE1} LICENSE
for j in $(find . -name "*.jar"); do
        mv $j $j.no
done
%mvn_file : %{parent}/%{subname}
%{?scl:EOF}

%build
%{?scl:scl enable %{scl_java_common} %{scl_maven} %{scl} - <<"EOF"}
set -e -x
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl_java_common} %{scl_maven} %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%dir %{_mavenpomdir}/plexus
%dir %{_javadir}/plexus
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Fri Jan 16 2015 Michal Srb <msrb@redhat.com> - 0:1.1.8-16.10
- Fix directory ownership

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 0:1.1.8-16.9
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 0:1.1.8-16.8
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.1.8-16.7
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.1.8-16.6
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.1.8-16.5
- Mass rebuild 2014-02-18

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.1.8-16.4
- Remove requires on java

* Mon Feb 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.1.8-16.3
- SCL-ize build-requires
- Migrate from mvn-rpmbuild to %%mvn_build

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.1.8-16.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.1.8-16.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 01.1.8-16
- Mass rebuild 2013-12-27

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.1.8-15
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.1.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 0:1.1.8-13
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Nov 22 2012 Jaromir Capik <jcapik@redhat.com> - 0:1.1.8-12
- Migration to plexus-containers-container-default

* Wed Nov 21 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.1.8-11
- Install LICENSE file
- Resolves: rhbz#878833

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.1.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.1.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Sep 7 2011 Alexander Kurtakov <akurtako@redhat.com> 0:1.1.8-8
- Drop ant build.
- Further cleanups.

* Thu Jul 28 2011 Jaromir Capik <jcapik@redhat.com> - 0:1.1.8-7
- Migration to maven3
- Removal of plexus-maven-plugin (not needed)
- Minor spec file changes according to the latest guidelines

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.1.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 22 2009 Alexander Kurtakov <akurtako@redhat.com> 0:1.1.8-5
- BR java-devel 1.6.

* Tue Dec 22 2009 Alexander Kurtakov <akurtako@redhat.com> 0:1.1.8-4
- BR maven-surefire-provider-junit.

* Tue Dec 22 2009 Alexander Kurtakov <akurtako@redhat.com> 0:1.1.8-3
- BR maven-doxia-sitetools.

* Tue Dec 22 2009 Alexander Kurtakov <akurtako@redhat.com> 0:1.1.8-2
- BR plexus-maven-plugin.

* Tue Dec 22 2009 Alexander Kurtakov <akurtako@redhat.com> 0:1.1.8-1
- Update to upstream 1.1.8.

* Fri Aug 21 2009 Andrew Overholt <overholt@redhat.com> 1.1.7-3.3
- Add ant-nodeps BR

* Fri Aug 21 2009 Andrew Overholt <overholt@redhat.com> 1.1.7-3.2
- Add ant-contrib BR

* Fri Aug 21 2009 Andrew Overholt <overholt@redhat.com> 0:1.1.7-3.1
- Import from Deepak Bhole's work (import from JPackage, update to 1.1.7)
- Remove gcj support

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.1.2-5.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.1.2-4.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jul  9 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0:1.1.2-3.2
- drop repotag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0:1.1.2-3jpp.1
- Autorebuild for GCC 4.3

* Sat Mar 24 2007 Ralph Apel <r.apel at r-apel.de> - 0:1.1.2-3jpp
- Build with maven2 by default
- Add gcj_support options

* Fri Feb 16 2007 Tania Bento <tbento@redhat.com> - 0:1.1.2-2jpp.1
- Fixed %%License.
- Fixed %%BuildRoot.
- Fixed %%Release.
- Removed the %%post and %%postun for javadoc.
- Removed %%Vendor.
- Removed %%Distribution.
- Removed "%%define section free".
- Added the gcj support option.
- Added BR for jakarta-commons-logging.

* Wed May 17 2006 Ralph Apel <r.apel at r-apel.de> - 0:1.1.2-2jpp
- First JPP-1.7 release

* Mon Nov 07 2005 Ralph Apel <r.apel at r-apel.de> - 0:1.1.2-1jpp
- First JPackage build
