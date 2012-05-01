Minimal NS4600 module
================================

The Promise SmartStor NS4600 is great.  But have you ever wanted to remotely
start it up and shut it down without having to touch the web UI? Well, now you
can do just that with this module.

Usage
-----

Control your NS4600 with ease::

    import ns4600

    # wake up NAS (must enable Wake-On-LAN on device)
    ns4600.wake('00:01:02:03:04:05')
        ...

    # shut down NAS
    ns4600.shutdown('admin','password','http://my-ns4600.local')

Installation
------------

Installing the ns4600 module is simple::

    $ pip install ns4600
