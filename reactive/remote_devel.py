from charms.reactive import when, when_not, set_state


@when_not('remote-devel.installed')
def install_remote_devel():
    set_state('remote-devel.installed')
