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


def display_dict(data, offset):
    r = []

    def display(d, off):
        for key, val in sorted(d.items()):
            if not isinstance(val, dict):
                r.append('{}  {}: {}'.format(off, key, val))
            else:
                r.append('{}  {}: {}'.format(off, key, '{'))
                new_off = off + ' ' * 4
                display(val, new_off)
                r.append('{}{}'.format(off + ' ' * 2, '}'))
        return '\n'.join(r)
    return display(data, offset)


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
            node_type = node[diff.TYPE]
            node_value = node[diff.VALUE]
            if node_type == diff.CHANGED:
                if not isinstance(node_value, dict):
                    res.append('{}{} {}: {}'.format(offset, ADDED, key, bool2json(node_value)))
                    if not isinstance(node[diff.OLD_VALUE], dict):
                        res.append('{}{} {}: {}'.format(offset, REMOVED, key, bool2json(node[diff.OLD_VALUE])))
                    else:
                        res.append('{}{} {}: {}'.format(offset, REMOVED, key, '{'))
                        new_offset = offset + ' ' * 4
                        res.append(display_dict(node[diff.OLD_VALUE], new_offset))
                        res.append('{}{}'.format(offset + ' ' * 2, '}'))
                else:
                    res.append('{}{} {}: {}'.format(offset, ADDED, key, '{'))
                    new_offset = offset + ' ' * 4
                    res.append(display_dict(node_value, new_offset))
                    res.append('{}{}'.format(offset + ' ' * 2, '}'))
                    res.append('{}{} {}: {}'.format(offset, REMOVED, key, bool2json(node[diff.OLD_VALUE])))
            if node_type in (diff.ADDED, diff.REMOVED, diff.SAVED):
                if not isinstance(node_value, dict):
                    res.append('{}{} {}: {}'.format(offset, set_symb()[node_type], key, bool2json(node_value)))
                else:
                    res.append('{}{} {}: {}'.format(offset, set_symb()[node_type], key, '{'))
                    new_offset = offset + ' ' * 4
                    res.append(display_dict(node_value, new_offset))
                    res.append('{}{}'.format(offset + ' ' * 2, '}'))
            if node_type == diff.NESTED:
                res.append('{}{} {}: {}'.format(offset, SAVED, key, '{'))
                new_offset = offset + ' ' * 4
                view_default(node_value, new_offset)
                res.append('{}{}'.format(offset + ' ' * 2, '}'))
    view_default(data, offset)
    res.append('}')
    return '\n'.join(res)
