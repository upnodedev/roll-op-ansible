roll-op-ansible
=========

An ansible script to simplify OP Stack deployment process using https://github.com/0xFableOrg/roll-op

Requirements
------------

Recommended specification
* 8 CPUs
* 32 GB RAM
* 512+ GB SSD or NVME disk

Role Variables
--------------

* `roll_op_status` - The status of the l1 and l2 services at the end of installation (Required, should be started, restarted, stopped) 
* `roll_op_rollup_name` - Rollup name (Default: getting-started)
* `roll_op_clean` - If true, cleans up deployment outputs and databases before launching services (Default: false)
* `roll_op_preset` - The preset rollup configuration to use (dev or prod) (Default: dev)
* `roll_op_l1_rpc` - L1 RPC endpoint (Optional, if not supplied, will launch a devnet)
* `roll_op_l2_chain_id` - L2 Chain ID (Default: 42069)
* `roll_op_seed_phrase` - Seed phrase to generate admin, batcher, proposer, and sequencer accounts (Default: test ... junk)
* `roll_op_seed_phrase_language` - Language used in seed phrase (Default: english)
* `roll_op_admin_key` - Admin account private key
* `roll_op_batcher_key` - Batcher account private key
* `roll_op_proposer_key` - Proposer account private key
* `roll_op_p2p_sequencer_key` - Sequencer account private key

Note: Either a seed phrase or all 4 account keys should be provided, but not both. If neither are provided, the default seedphrase (test ... junk) will be used.

More information about Rollup Name, Clean, and Config Preset are available at https://github.com/0xFableOrg/roll-op

Dependencies
------------

- [tobias_richter.apt_upgrade](https://github.com/tobias-richter/ansible-apt-upgrade)
- [geerlingguy.pip](https://github.com/geerlingguy/ansible-role-pip) to install pip on the machine

Example Playbooks
-----------------

To install using only default parameters (the dev preset and the 'test ... junk' seedphrase)

    - hosts: servers
      roles:
         - role: upnodedev.op.roll_op
      vars:
        roll_op_status: started           

To use a specified seedphrase

    - hosts: servers
      roles:
         - role: upnodedev.op.roll_op
      vars:
        roll_op_status: started   
        roll_op_seed_phrase: 'test test test test test test test test test test test junk'       

To use an external l2 rpc

    - hosts: servers
      roles:
         - role: upnodedev.op.roll_op
      vars:
        roll_op_status: started
        roll_op_l1_rpc: 'https://eth-sepolia.g.alchemy.com/v2/...<ALCHEMY_API_KEY>...' 
        roll_op_seed_phrase: 'test test test test test test test test test test test junk'

To use specified private keys in place of a seedphrase

    - hosts: servers
      roles:
         - role: upnodedev.op.roll_op
      vars:
        roll_op_status: started
        roll_op_admin_key: a##############################################################0
        roll_op_batcher_key: a##############################################################0
        roll_op_proposer_key: a##############################################################0
        roll_op_p2p_sequencer_key: a##############################################################0


License
-------

BSD 3-Clause License
