# Team Fortress2: cfg syncer

Team Fortress cfg files sync


## HOW TO SETUP

**Requirements:**
- [Git client](https://git-scm.com/downloads): if you wish push changes back to remote repository, otherwise just download the project (zip compressed)
- [Bitbucket](bitbucket.org/), [Github](github.com) (recommend) account or whatever like that
- [Python v3.7+](https://www.python.org/downloads/)


Fork and then git clone the repository, i.e.:

```bash
git clone git@github.com:felipsmartins/teamfortress2-config.git
```

## HOW TO RUN

```bash
$ python3 teamfortress2-config/install.py --help
usage: install.py [-h] steamapps_dir

Sync files to Team Fortress directory

positional arguments:
  steamapps_dir  Absolute path to 'steamapps' directory

optional arguments:
  -h, --help     show this help message and exit

# then:
$ python3 teamfortress2-config/install.py ~/.steam/steam/steamapps
```

_Output example_: 

![output](doc/output.png)



## TODO:

- Dropbox integration
- Google Drive integration
<hr>

My steam profile: https://steamcommunity.com/id/felipsmartins/