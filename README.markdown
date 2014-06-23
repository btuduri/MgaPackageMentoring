MgaPackageMentoring
===================

Work in progress on the mageia packaging mentoring.

Directories :
============

archives :
  it will be use to import fedora or mandriva packages into mageia.

rpm :
  it my working directory.

How build a package :
====================

_Only zzuf and milkutracker 0.90.85 are buildable_

_Before you need to have a rpmbuild up to date and correctly configured for Mageia system. (cf the mageia wiki)._

Milkytracker 0.90.85 :
---------------------
1. Open archives directory :

    cd archives

2. Download the fedora package :

```
    $ wget `cat milkytracker-0.90.85-8.fc21.src.rpm.download-url`
```

```
    $ sha512sum -c milkytracker-0.90.85-8.fc21.src.rpm.download-url.sha512
```

```
    $ milkytracker-0.90.85-8.fc21.src.rpm: OK
```

3. Install the fedora rpm in your packaging workspace :

```
    $ rpm -Uvh milkytracker-0.90.85-8.fc21.src.rpm
```

4. Replace the fedora SPEC file by the one of this repository :

```
    $ cd ../rpm
```

```
    $ cp ./milkytracker.spec $HOME/rpmbuild/SPEC
```

5. Go to the rpmbuild SPEC directory :

```
    $ cd $HOME/rpmbuild/SPEC
```

6. Download the dependancies :

```
    $ sudo urpmi milkytracker.spec
```

7. Build the package :

```
    $ bm -l milkytracker.spec
```
