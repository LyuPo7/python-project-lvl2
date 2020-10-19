# This Python file uses the following encoding: utf-8

"""Default view module."""
from gendiff import diff

# Constants
SAVED = ' '
ADDED = '+'
REMOVED = '-'


def bool2json(value):
    """Convert Python bool to json bool

    Args:
        value(str): value for convert

    Returns:
        value(str): converted value.
        """
    if isinstance(value, bool):
        return str(value).lower()
    return value


def set_symb():
    return {
        diff.SAVED: SAVED,
        diff.ADDED: ADDED,
        diff.REMOVED: REMOVED,
    }


def view(data):
    """View in dict format difference between 2 files.

    Views in dict format difference between 2 files.

    Args:
        diff(dict): difference between 2 files in dict format

    Returns:
        str - difference between 2 files in str format.
    """
    res = []
    offset = '  '
    res.append('{')

    def view_default(dict4view, offset):
        """Check and print dictionary in dict format.

        Checks if values of the dictionary are dictionaries too:
        if so calls recursively itself,
        in other case print value in dict format.

        Args:
            dict4view(dict): dictionary for check,
            offset(str): offset for print value.
        """
        for key, node in sorted(dict4view.items()):
            if isinstance(node, dict):
                node_type = node.get(diff.TYPE)
                node_value = node.get(diff.VALUE)
                if node_type:
                    if not isinstance(node_value, dict):
                        if node_type == diff.CHANGED:
                            res.append('{}{} {}: {}'.format(offset, ADDED, key, bool2json(node_value)))
                            if not isinstance(node[diff.OLD_VALUE], dict):
                                res.append('{}{} {}: {}'.format(offset, REMOVED, key, bool2json(node[diff.OLD_VALUE])))
                            else:
                                res.append('{}{} {}: {}'.format(offset, REMOVED, key, '{'))
                                new_offset = offset + ' ' * 4
                                view_default(node[diff.OLD_VALUE], new_offset)
                                res.append('{}{}'.format(offset + ' ' * 2, '}'))
                        else:
                            res.append('{}{} {}: {}'.format(offset, set_symb()[node_type], key, bool2json(node_value)))
                    else:
                        if node_type == diff.CHANGED:
                            res.append('{}{} {}: {}'.format(offset, ADDED, key, '{'))
                            new_offset = offset + ' ' * 4
                            view_default(node_value, new_offset)
                            res.append('{}{}'.format(offset + ' ' * 2, '}'))
                            if not isinstance(node[diff.OLD_VALUE], dict):
                                res.append('{}{} {}: {}'.format(offset, REMOVED, key, bool2json(node[diff.OLD_VALUE])))
                            else:
                                res.append('{}{} {}: {}'.format(offset, REMOVED, key, '{'))
                                new_offset = offset + ' ' * 4
                                view_default(node[diff.OLD_VALUE], new_offset)
                                res.append('{}{}'.format(offset + ' ' * 2, '}'))
                        else:
                            res.append('{}{} {}: {}'.format(offset, set_symb()[node_type], key, '{'))
                            new_offset = offset + ' ' * 4
                            view_default(node_value, new_offset)
                            res.append('{}{}'.format(offset + ' ' * 2, '}'))
                else:
                    if not isinstance(node, dict):
                        res.append('{}  {}: {}'.format(offset, key, bool2json(node)))
                    else:
                        res.append('{}  {}: {}'.format(offset, key, '{'))
                        new_offset = offset + ' ' * 4
                        view_default(node, new_offset)
                        res.append('{}{}'.format(offset + ' ' * 2, '}'))
            else:
                res.append('{}  {}: {}'.format(offset, key, bool2json(node)))
    view_default(data, offset)
    res.append('}')
    return '\n'.join(res)
