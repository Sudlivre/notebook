
# MongoEngine Document

## 数据库查询

`Document `对象有一个 `objects` 属性，用来访问在数据库中跟这个类有关的对象。这个` objects `属性其实是一个`QuerySetManager` ，
它会创建和返回一个新的 `QuerySet `对象的访问。这个` QuerySet `对象可以从数据库中遍历获取的文档：
```
# Prints out the names of all the users in the database
for user in User.objects:
    print user.name
```

### 过滤查询

可以通过调用 `QuerySet `对象的关键字参数来对数据查询进行过滤，关键字查询中的键和你想要查询的`Document`中的字段一致：
```
# This will return a QuerySet that will only iterate over users whose
# 'country' field is set to 'uk'
uk_users = User.objects(country='uk')
```

对于内嵌document的字段可以使用` __ `来代替对象属性访问语法中的` . `进行访问：
```
# This will return a QuerySet that will only iterate over pages that have
# been written by a user whose 'country' field is set to 'uk'
uk_pages = Page.objects(author__country='uk')
```
### 查询操作符

在查询中也可以使用操作符，只要将其加在关键字的双下划线之后即可：
```
# Only find users whose age is 18 or less
young_users = Users.objects(age__lte=18)
```
可用的运算符如下：
```
ne – 不等于≠
lt – 小于<
lte – 小于等于≤
gt – 大于>
gte – 大于等于 ≥
not – 否定一个标准的检查，需要用在其他操作符之前(e.g. Q(age__not__mod=5))
in – 值在 list 中
nin – 值不在 list 中
mod – value % x == y, 其中 x 和 y 为给定的值
all – list 里面所有的值
size – 数组的大小
exists – 存在这个值
```

字符串查询

以下操作符可以快捷的进行正则查询：
```
exact – 字符串型字段完全匹配这个值
iexact – 字符串型字段完全匹配这个值（大小写敏感）
contains – 字符串字段包含这个值
icontains – 字符串字段包含这个值（大小写敏感）
startswith – 字符串字段由这个值开头
istartswith – 字符串字段由这个值开头（大小写敏感）
endswith – 字符串字段由这个值结尾
iendswith – 字符串字段由这个值结尾（大小写敏感）
match – 执行 $elemMatch 操作，所以你可以使用一个数组中的 document 实例
```

地理查询

PASS

列表查询

对于大多数字段，这种语法会查询出那些字段与给出的值相匹配的`document`，但是当一个字段引用` ListField` 的时候，而只会提供一条数据，那么包含这条数据的就会被匹配上：
```
class Page(Document):
    tags = ListField(StringField())

# This will match all pages that have the word 'coding' as an item in the
# 'tags' list
Page.objects(tags='coding')
```

原始查询

你可以通过` __raw__ `参数来使用一个原始的 PyMongo 语句来进行查询，这样可以进行原始的完整查询：
```
Page.objects(__raw__={'tags': 'coding'})
```

### 限制和跳过结果

就像传统的ORM一样，你有时候需要限制返回的结果的数量，或者需要跳过一定数量的结果。`QuerySet `里面可以使用` limit()` 和 `skip() `这两个方法来实现，但是更推荐使用数组切割的语法：
```
# Only the first 5 people
users = User.objects[:5]

# All except for the first 5 people
users = User.objects[5:]

# 5 users, starting from the 11th user found
users = User.objects[10:15]
```
你可以指定让查询返回一个结果。如果这个条在数据库中不存在，那么会引发 `IndexError `错误 。使用 `first()` 方法在数据不存在的时候会返回` None`：
```
>>> # Make sure there are no users
>>> User.drop_collection()
>>> User.objects[0]
IndexError: list index out of range
>>> User.objects.first() == None
True
>>> User(name='Test User').save()
>>> User.objects[0] == User.objects.first()
True
```

### 默认Document 查询

默认情况下，`Document`的`objects` 属性返回一个一个 `QuerySet` 对象，它并没有进行任何筛选和过滤，它返回的是所有的数据对象。
这一点可以通过给一个 `document `定义一个方法来修改 一个`queryset `。这个方法需要两参数`__doc_cls` 和 `queryset` 。
第一个参数是定义这个方法的 `Document `类名（从这个意义上来说，这个方法像是一个` classmethod()` 而不是一般的方法），
第二个参数是初始化的 `queryset`。这个方法需要使用 `queryset_manager()`来装饰来它，使得它被认可。
```
class BlogPost(Document):
    title = StringField()
    date = DateTimeField()

    @queryset_manager
    def objects(doc_cls, queryset):
        # This may actually also be done by defining a default ordering for
        # the document, but this illustrates the use of manager methods
        return queryset.order_by('-date')
```
你不用调用` objects` 方法，你可以自定义更多的管理方法，例如：
```
class BlogPost(Document):
    title = StringField()
    published = BooleanField()

    @queryset_manager
    def live_posts(doc_cls, queryset):
        return queryset.filter(published=True)

BlogPost(title='test1', published=False).save()
BlogPost(title='test2', published=True).save()
assert len(BlogPost.objects) == 2
assert len(BlogPost.live_posts()) == 1
```

### 自定义 `QuerySets`

当你想自己定义一些方法来过滤 `document `的时候，继承` QuerySet `类对你来说就是个好的方法。
为了在 `document` 里面使用一个自定义的` QuerySet `类，你可以在 `document` 里的 `meta `字典里设置` queryset_class` 的值来实现它。

```
class AwesomerQuerySet(QuerySet):

    def get_awesome(self):
        return self.filter(awesome=True)

class Page(Document):
    meta = {'queryset_class': AwesomerQuerySet}

# To call:
Page.objects.get_awesome()
```

### Aggregation 聚合

MongoDB 提供了开箱即用的聚合方法，但没有 RDBMS 提供的那样多。MongoEngine 提供了一个包装过的内置的方法，同时自身提供了一些方法，它实现了在数据库服务上执行的 Javascript 代码的功能。

结果计数
就像限制和跳过结果一样， QuerySet 对象提供了用来计数的方法 - count()，不过还有一个更 Pythonic 的方法来实现：
```
num_users = len(User.objects)
```

更多功能

当你想为 `document` 的特定的字段的数量计数的时候，可以使用 `sum()`：
```
yearly_expense = Employee.objects.sum('salary')
```
当你想求某个字段的平均值的时候，可以使用` average()`：
```
mean_age = User.objects.average('age')
```
MongoEngine 提供了一个方法来获取一个在集合里 item 的频率 - item_frequencies()。下面一个例子可以生成 tag-clouds：
```
class Article(Document):
    tag = ListField(StringField())

# After adding some tagged articles...
tag_freqs = Article.objects.item_frequencies('tag', normalize=True)

from operator import itemgetter
top_tags = sorted(tag_freqs.items(), key=itemgetter(1), reverse=True)[:10]
```

### 查询效率和性能
PASS

### 高级查询
有时候使用关键字参数返回的 `QuerySet` 不能完全满足你的查询需要。例如有时候你需要将约束条件进行`and`，`or` 的操作。
你可以使用` MongoEngine `提供的 `Q `类来实现，一个 `Q` 类代表了一个查询的一部分，里面的参数设置与你查询`document `的时候相同。
建立一个复杂查询的时候，你需要用 `& `或 `|` 操作符将 `Q` 对象连结起来。例如：
```
from mongoengine.queryset.visitor import Q

# Get published posts
Post.objects(Q(published=True) | Q(publish_date__lte=datetime.now()))

# Get top posts
Post.objects((Q(featured=True) & Q(hits__gte=1000)) | Q(hits__gte=5000))
```

### Atomic updates（原子更新）

MongoDB 文档 可以通过`QuerySet` 上的 `update_one()`、`update()`、`modify()` 方法自动更新。下面几种操作符可以被用到这几种方法上：
```
set – 设置成一个指定的值
unset – 删除一个指定的值
inc – 将值加上一个给定的数
dec – 将值减去一个给定的数
push – 在 list 中添加一个值
push_all – 在 list 中添加一个值
pop – 移除list 的第一项或最后一项（根据 pop__<field>=val 中val 的值决定删除第一项还是最后一项，一般情况下，val 为负则删除第一项，为正则删除最后一项，参见：mongodb $pop
pull – 从 list 里面移除一个值
pull_all – 从 list 里面移除个值
add_to_set – 当要添加的值不在 list 中时，添加这个值
```

原子更新的语法类似于查询语法，区别在于修饰操作符位于字段之前，而不是之后：
```
>>> post = BlogPost(title='Test', page_views=0, tags=['database'])
>>> post.save()
>>> BlogPost.objects(id=post.id).update_one(inc__page_views=1)
>>> post.reload()  # the document has been changed, so we need to reload it
>>> post.page_views
1
>>> BlogPost.objects(id=post.id).update_one(set__title='Example Post')
>>> post.reload()
>>> post.title
'Example Post'
>>> BlogPost.objects(id=post.id).update_one(push__tags='nosql')
>>> post.reload()
>>> post.tags
['database', 'nosql']
```
如果没有修饰操作符，则默认为`$set`：
```
BlogPost.objects(id=post.id).update(title='Example Post')
BlogPost.objects(id=post.id).update(set__title='Example Post')
```

### 服务器端 `JavaScript` 执行
可以写 `Javascript`函数，然后发送到服务器来执行。它返回结果是 `Javascript` 函数的返回值。这个功能是通过`QuerySet()`对象的`exec_js()`
方法实现。传递一个包含一个`Javascript`函数的字符串作为第一个参数。

其余位置的参数的名字字段将作为您的`Javascript`函数的参数传递过去。

在` JavaScript `函数范围中，一些变量可用：
- `collection` – 对应使用的` Document` 类的集合的名称
- query – 一个 QuerySet 对象
- `options` – 一个对象，它包含要传递给 `exec_js()` 函数的一些参数
```
def sum_field(document, field_name, include_negatives=True):
    code = """
    function(sumField) {
        var total = 0.0;
        db[collection].find(query).forEach(function(doc) {
            var val = doc[sumField];
            if (val >= 0.0 || options.includeNegatives) {
                total += val;
            }
        });
        return total;
    }
    """
    options = {'includeNegatives': include_negatives}
    return document.objects.exec_js(code, field_name, **options)
```