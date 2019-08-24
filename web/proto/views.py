from django.views import generic
from .models import Spot
from .forms import SpotSearchForm

class IndexView(generic.TemplateView):
    template_name = 'proto/proto_list.html'

class SearchView(generic.ListView):
    model = Spot

    def get_context_data(self):
        """テンプレートへ渡す辞書の作成"""
        context = super().get_context_data()
        context['form'] = SpotSearchForm(self.request.GET)
        return context

    def get_queryset(self):
        """テンプレートへ渡す「prefecture_list」を作成する"""
        form = SpotSearchForm(self.request.GET)
        form.is_valid()

        queryset = super().get_queryset()

        # 都道府県の選択があれば、絞り込み(filter)
        prefecture = form.cleaned_data['prefecture']
        if prefecture:
            queryset = queryset.filter(prefecture=prefecture)

        return queryset
