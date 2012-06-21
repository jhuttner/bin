# My bin commands

    $ up $dir

    # Search directories above the current directory for one which contains
    # $dir as a substring.  If found, cd to it.  If not found, do nothing.
    
    # If starting out in the /usr/local/adnxs/api directory for each command...

    $ up adnxs => you're in /usr/local/adnxs.
    $ up nxs => you're in /usr/local/adnxs (nxs is in adnxs).
    $ up foo => you stay put.



    $ versiongrab

    # List the current versions for AppNexus API endpoints.
