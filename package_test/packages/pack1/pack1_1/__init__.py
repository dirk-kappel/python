


# After importing this package - import pack1.pack1_1
# pack1.__package__ = pack1
# pack1.__path__ = ['/home/wsl2/python/package_test/packages/pack1']
# pack1.__file__ = '/home/wsl2/python/package_test/packages/pack1/__init__.py'


print('executing pack1_1...')

value = 'pack1_1 value'
# To fetch value pack1.pack1_1.value


# You can load(import) sub modules in the code here.
import pack1.pack1_1.module1_1a  # need to have the full path here to import
import pack1.pack1_1.module1_1b