"""
This is a dictionary utility that will take a passed in dictionary and match it up with a schema dictionary.
If the passed in dictionary doesn't contain all of the keys that the schema dictionary does it will return True
indication that the dictionary is indeed missing keys.

Developed as part of work on Anthropologie Replatform in 2016 as member of Urban Outfitters UI Engineering Group
"""

def is_missing_keys(required_dict, actual_dict):
    """
    :param required_dict: required keys to check for
    :param actual_dict: dictionary to check for key inside
    :return bool
    """
    missing_keys = []

    def does_key_exist (key, dictionary):
        """
        Append key name to missing keys if it isn't in the dictionary
        :param key: key to check for existence
        :param dictionary: dictionary to check for key inside
        """
        if not key in dictionary.keys() or dictionary[key] == None:
            missing_keys.append(key)

    def is_key_a_dict (key, dictionary):
        """
        Check key in dictionary to see if it has sub keys
        :param key: key to check for sub keys
        :param dictionary: dictionary that key is in
        :return bool
        """
        return isinstance(dictionary[key], dict)

    def check_for_keys_in_dict(required, actual):
        """
        Handles looping through current tier of dictionary
        and calls checks on the keys inside of it
        :param required: dictionary of required keys
        :param actual: dictionary to test against
        """
        for key in required.keys():
            does_key_exist(key, actual)

            # check current key for sub keys
            # if it has subkeys, check for existence of sub keys
            if is_key_a_dict(key, required):
                check_for_keys_in_dict(required[key], actual[key])

    # start checking required keys at root level
    check_for_keys_in_dict(required_dict, actual_dict)

    if len(missing_keys) > 0:
        logger.warn('MISSING KEYS IN DICT ~~~ ' + str(missing_keys))
        return True

    return False
