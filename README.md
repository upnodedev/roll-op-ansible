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

* `roll_op_l1_rpc` - L1 RPC Endpoint (Optional, if not supplied, will launch a devnet)
* `roll_op_l2_chain_id` - L2 Chain ID (Default: 42069)
* `roll_op_seed_phrase` - Seed phrase to generate Admin, Batcher, Proposer, and Sequencer (Default: test ... junk)
* `roll_op_seed_phrase_language` - Language used in seed phrase (Default: english)
* `roll_op_admin_key` - Admin private key
* `roll_op_batcher_key` - Batcher private key
* `roll_op_proposer_key` - Proposer private key
* `roll_op_p2p_sequencer_key` - Sequencer private key
* `roll_op_rollup_name` - Rollup Name (Default: getting-started)
* `roll_op_clean` - Clean (Default: false)
* `roll_op_preset` - Config Preset (dev or prod) (Default: dev)

Note: Seed phrase and private keys can't be provided at the same time.

More information about Rollup Name, Clean, and Config Preset are available at https://github.com/0xFableOrg/roll-op

Dependencies
------------

- [geerlingguy.pip](https://github.com/geerlingguy/ansible-role-pip) to install pip on the machine

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - role: upnodedev.roll-op-ansible
           

License
-------

BSD 3-Clause License
