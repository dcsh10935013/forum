from django.views.generic import *
from django.urls import reverse
from .models import *

# 討論主題列表
class TopicList(ListView):#listview自己改名成Topiclist
    model = Topic
    ordering = ['-created'] #用created(建立時間)排序(加負號為倒敘)
    paginate_by = 20        # 每頁主題數(最多一頁幾筆)

# 新增討論主題
class TopicNew(CreateView):
    model = Topic
    fields = ['subject', 'content']#使用者要哪些欄位

    def get_success_url(self):#新增完主題回列表
        return reverse('topic_list')

    def form_valid(self, form):#驗證表班是否有缺並補足
        # 自動將目前使用者填入討論主題的作者欄
        form.instance.author = self.request.user
        return super().form_valid(form)#補足完丟回Form處存

# 檢視討論主題
class TopicView(DetailView):
    model = Topic