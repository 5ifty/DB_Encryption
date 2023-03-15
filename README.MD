This is a project for my college course:
Theres a few things I'd like to tweak, but Im in a limited time frame and really haven't got the time to refactor, such as the raw file paths- it's janky and unclean but for now it works
The main process of this is -> Convert xlsx file to a Json, then to a Json Dict. -> Encrypt this Json Dict -> Delete the unencrypted Dict -> Then initialise the database upload data and decrypt on a correct Passphrase/Key.
