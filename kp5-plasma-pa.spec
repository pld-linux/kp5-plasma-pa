%define		kdeplasmaver	5.22.2.1
%define		qtver		5.9.0
%define		kpname		plasma-pa

Summary:	KDE Plasma Pulse Audio
Name:		kp5-%{kpname}
Version:	5.22.2.1
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	1d0218239f3dc556e1708483d44155b8
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	fontconfig-devel
BuildRequires:	kf5-attica-devel
BuildRequires:	kf5-kactivities-stats-devel
BuildRequires:	kf5-kauth-devel
BuildRequires:	kf5-kcmutils-devel
BuildRequires:	kf5-kdbusaddons-devel
BuildRequires:	kf5-kdeclarative-devel
BuildRequires:	kf5-kdelibs4support-devel
BuildRequires:	kf5-kdoctools-devel
BuildRequires:	kf5-kglobalaccel-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-knewstuff-devel
BuildRequires:	kf5-knotifications-devel
BuildRequires:	kf5-knotifyconfig-devel
BuildRequires:	kf5-kpeople-devel
BuildRequires:	kf5-krunner-devel
BuildRequires:	kf5-kwallet-devel
BuildRequires:	kf5-plasma-framework-devel
BuildRequires:	ninja
BuildRequires:	pulseaudio-devel
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	xorg-driver-input-evdev-devel
BuildRequires:	xorg-driver-input-synaptics-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xz
Suggests:	perl-base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
KDE Plasma Pulse Audio.

%prep
%setup -q -n %{kpname}-%{version}

%build
install -d build
cd build
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	../
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kpname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{kpname}.lang
%defattr(644,root,root,755)
%{_libdir}/qt5/plugins/kcms/kcm_pulseaudio.so
%dir %{_libdir}/qt5/qml/org/kde/plasma/private/volume
%{_libdir}/qt5/qml/org/kde/plasma/private/volume/PulseObjectFilterModel.qml
%{_libdir}/qt5/qml/org/kde/plasma/private/volume/libplasma-volume-declarative.so
%{_libdir}/qt5/qml/org/kde/plasma/private/volume/qmldir
%{_datadir}/kconf_update/disable_kmix.upd
%attr(755,root,root) %{_datadir}/kconf_update/plasmaVolumeDisableKMixAutostart.pl
%dir %{_datadir}/kde4/apps
%dir %{_datadir}/kde4/apps/kconf_update
%{_datadir}/kde4/apps/kconf_update/disable_kmix.upd
%attr(755,root,root) %{_datadir}/kde4/apps/kconf_update/plasmaVolumeDisableKMixAutostart.pl
%dir %{_datadir}/kpackage/kcms/kcm_pulseaudio
%dir %{_datadir}/kpackage/kcms/kcm_pulseaudio/contents
%dir %{_datadir}/kpackage/kcms/kcm_pulseaudio/contents/ui
%{_datadir}/kpackage/kcms/kcm_pulseaudio/contents/ui/Advanced.qml
%{_datadir}/kpackage/kcms/kcm_pulseaudio/contents/ui/CardListItem.qml
%{_datadir}/kpackage/kcms/kcm_pulseaudio/contents/ui/DeviceComboBox.qml
%{_datadir}/kpackage/kcms/kcm_pulseaudio/contents/ui/DeviceListItem.qml
%{_datadir}/kpackage/kcms/kcm_pulseaudio/contents/ui/MuteButton.qml
%{_datadir}/kpackage/kcms/kcm_pulseaudio/contents/ui/StreamListItem.qml
%{_datadir}/kpackage/kcms/kcm_pulseaudio/contents/ui/VolumeSlider.qml
%{_datadir}/kpackage/kcms/kcm_pulseaudio/contents/ui/main.qml
%{_datadir}/kpackage/kcms/kcm_pulseaudio/metadata.desktop
%{_datadir}/kpackage/kcms/kcm_pulseaudio/metadata.json
%{_datadir}/kservices5/kcm_pulseaudio.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.volume.desktop
%{_datadir}/metainfo/org.kde.plasma.volume.appdata.xml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.volume
%{_datadir}/plasma/plasmoids/org.kde.plasma.volume/contents.rcc
%{_datadir}/plasma/plasmoids/org.kde.plasma.volume/metadata.json
%dir %{_datadir}/kpackage/kcms/kcm_pulseaudio/contents/code
%{_datadir}/kpackage/kcms/kcm_pulseaudio/contents/code/icon.js
