# add efi
 #1. dosfstools 
 http://www.linuxfromscratch.org/blfs/view/svn/postlfs/dosfstools.html

 #2. popt
 http://www.linuxfromscratch.org/blfs/view/svn/general/popt.html
 
 #3. efivar-37
 https://github.com/rhboot/efivar/releases/download/37/efivar-37.tar.bz2
 
 Required patch:
 http://svn.linuxfromscratch.org/patches/trunk/efivar/efivar-37-gcc_9-1.patch
 
 Make.defaults:
   Original Line:
   #CFLAGS ?= $(OPTIMIZE) -g3
   Line with the new FLAG:
   #CFLAGS ?= $(OPTIMIZE) -g3 -flto -flto-partition=none
 
 patch -Np1 -i ../efivar-37-gcc_9-1.patch
 make libdir=/usr/lib
 make libdir=/usr/lib install
 
 #4. EFIBOOTMGR-17
 https://github.com/rhboot/efibootmgr/archive/17/efibootmgr-17.tar.gz
 sed -e '/extern int efi_set_verbose/d' -i src/efibootmgr.c
 make sbindir=/sbin EFIDIR=LFS
 make sbindir=/sbin EFIDIR=LFS
 
 #5. UNIFONT-13.0.03
 http://unifoundry.com/pub/unifont/unifont-13.0.03/font-builds/unifont-13.0.03.pcf.gz
 mkdir -pv /usr/share/fonts/unifont &&
    gunzip -c unifont-13.0.03.pcf.gz > \
     /usr/share/fonts/unifont/unifont.pcf
 
 #6. Grub 2.04
 
 ./configure --prefix=/usr  \
        --sbindir=/sbin        \
        --sysconfdir=/etc      \
        --disable-efiemu       \
        --with-platform=efi    \
        --disable-werror
