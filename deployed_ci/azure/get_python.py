import argparse
import os.path
import shutil
import sys


shutil_error = getattr(shutil, 'SameFileError', shutil.Error)


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.set_defaults(func=parser.print_help)

    parser.add_argument(
        '--python-binary',
    )
    parser.add_argument(
        '--target-name',
    )
    parser.add_argument(
        '--version',
    )

    args = parser.parse_args()

    path = os.path.dirname(args.python_binary)
    _, extension = os.path.splitext(args.python_binary)
    version = args.version.split('.')

    targets = [os.path.join(path, 'python' + extension)]

    for i in range(len(version) + 1):
        version_text = '.'.join(version[:i])
        target = os.path.join(
            path,
            args.target_name + version_text + extension,
        )

        targets.append(target)

    for target in targets:
        print('copying: {!r} -> {!r}'.format(
            args.python_binary,
            target,
        ))

        try:
            shutil.copy(args.python_binary, target)
        except shutil_error:
            print('         same file')


sys.exit(main())
