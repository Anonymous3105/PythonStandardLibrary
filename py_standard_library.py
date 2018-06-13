# import string
# values = { 'var':'foo' }

# t = string.Template("""
# Variable	: $var
# Escape	: $$
# Variable in text: ${var}iable
# """)

# print 'TEMPLATE:', t.substitute(values)

# s = """
# Variable	: %(var)s
# Escape	: %%
# Variable in text: %(var)siable
# """
# print 'INTERPOLATION:', s % values

# -----------------------------------------------------------------------------------------------------------

# import textwrap
# sample_text =  """The textwrap module can be used to format text for output in situations where pretty-printing is desired. It offers Text
# programmatic functionality similar to the paragraph wrapping or filling features found in many text editors."""

# print "No dedent:\n"
# print textwrap.fill(sample_text, width=50)

# dedented_text = textwrap.dedent(sample_text)
# print 'Dedented:\n'
# print dedented_text

# dedented_text = textwrap.dedent(sample_text).strip()
# for width in [ 45, 70 ]:
# 	print '%d Columns:\n' % width
# 	print textwrap.fill(dedented_text, width=width)
# 	print

# -----------------------------------------------------------------------------------------------------------

# import re
# pattern = 'this'
# text = 'Does this text match the pattern?'
# match = re.search(pattern, text)
# s = match.start()
# e = match.end()
# print 'Found "%s"\nin "%s"\nfrom %d to %d ("%s")' % \
# (match.re.pattern, match.string, s, e, text[s:e])


# -----------------------------------------------------------------------------------------------------------

# import difflib
# # text1 = "Sint ut ullamco dolor nisi labore quis magna tempor quis ex consequat minim commodo deserunt sit eu mollit ullamco aliquip ea amet dolor ad aliqua voluptate nostrud consequat sed proident deserunt amet est magna duis nisi tempor non sint dolor cupidatat qui enim officia do reprehenderit excepteur eu adipisicing non pariatur mollit nostrud nulla ut exercitation ad ut et proident mollit in elit laboris cillum officia fugiat commodo elit fugiat duis voluptate est in culpa aliqua amet anim cillum magna ex et qui duis nisi quis nisi ullamco anim consectetur consectetur non sunt in in laborum amet ut dolor culpa sint sit ex commodo id ad sint duis ut in ullamco magna minim anim commodo consequat duis qui elit dolor officia incididunt duis ut officia laborum laborum reprehenderit elit consectetur est tempor aliqua nisi eu consequat elit anim et nulla irure et ad eiusmod qui irure in dolore officia proident minim reprehenderit dolor velit irure dolor duis aliquip officia voluptate et culpa commodo veniam dolore veniam officia in tempor dolor cillum deserunt sed dolor mollit proident cillum et dolore amet exercitation aliquip duis ad adipisicing irure veniam veniam consequat in fugiat ex aute duis est."
# # text2 = "Lorem ipsum est sit tempor nisi incididunt elit ea veniam ea nulla cupidatat sit incididunt consectetur dolore laborum sint ullamco ut voluptate dolore amet dolor quis eu culpa sunt eu dolore culpa dolor esse dolore ut pariatur reprehenderit irure quis in ut anim amet culpa ad non quis laborum ut enim adipisicing laborum consectetur et dolor dolore eiusmod mollit dolor nostrud excepteur labore sint irure magna tempor laborum dolor ad quis pariatur occaecat excepteur consequat cillum commodo dolore ut et ut voluptate nisi sit ut voluptate sit ullamco labore nulla duis nulla commodo dolore laborum laboris sint irure occaecat consectetur nulla irure dolor do consectetur duis labore cupidatat dolore veniam duis ut consequat in ut voluptate id elit commodo veniam culpa ut laboris incididunt reprehenderit pariatur officia in sint tempor proident incididunt occaecat dolor et culpa est officia aliqua minim enim dolor enim elit incididunt dolore magna non proident labore sit ut incididunt eu labore commodo velit adipisicing anim pariatur reprehenderit irure nulla proident sunt dolore duis culpa tempor proident mollit anim deserunt laborum occaecat fugiat duis magna nulla laborum magna dolore pariatur incididunt enim nostrud in sed aliqua sunt amet deserunt sunt occaecat veniam occaecat dolore velit aute sed veniam voluptate nulla aliquip esse magna minim nostrud magna reprehenderit est amet magna dolore sit est ad dolore proident sint minim dolore aliquip voluptate laborum laborum ex veniam officia ut dolore dolor dolore qui anim veniam ullamco officia esse excepteur dolor ut sed exercitation dolor aliqua do sint sunt tempor nulla excepteur aute occaecat nostrud tempor reprehenderit in amet proident non voluptate elit consectetur reprehenderit in adipisicing."

# text1 = "That is a text"
# text2 = "This is a test"

# d = difflib.Differ()

# diff = d.compare(text1, text2)
# diff = difflib.unified_diff(text1, text2, lineterm='',)

# print '\n'.join(diff)


# -----------------------------------------------------------------------------------------------------------

import collections

# print collections.Counter(['a', 'b', 'c', 'a', 'b', 'b'])
# print collections.Counter({'a':2, 'b':3, 'c':1})
# print collections.Counter(a=2, b=3, c=1)

# c = collections.Counter()
# print 'Initial :', c
# c.update('abcdaab')
# print 'Sequence:', c
# c.update({'a':1, 'd':5})
# print 'Dict:', c
# print(list(c.elements()))
# for letter in list(c.elements()):
# 	print '%s : %d' % (letter, c[letter])


# def default_factory():
# 	return 'default value'
# d = collections.defaultdict(default_factory, foo='bar')
# print d['foo'], d['pasta']


# d = collections.deque('abcdefg')
# print 'Deque:', d
# print 'Length:', len(d)
# d.remove('c')
# print d
# d.append('k')
# print d

# print 'From the right:'
# while True:
# 	try:
# 		print d.pop(),
# 	except IndexError:
# 		break

# d = collections.deque('abcdefg')
# print '\nFrom the left:'
# while True:
# 	try:
# 		print d.popleft(),
# 	except IndexError:
# 		break

# d = collections.deque('abcdefg')
# d.rotate(2)
# print '\nRight rotation:', d
# d.rotate(-2)
# print '\nLeft rotation :', d


# Person = collections.namedtuple('Person', 'name age gender')
# print 'Type of Person:', type(Person)
# bob = Person(name='Bob', age=30, gender='male')
# print bob
# print "%s is a %d years old %s person.\n" % bob





# -----------------------------------------------------------------------------------------------------------