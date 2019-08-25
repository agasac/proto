from django.views import generic
from django.shortcuts import render
from .models import Spot
from .forms import SpotSearchForm, JaranSearchForm
import requests
from bs4 import BeautifulSoup

api_key = "psc16cc2723f3d"
pref_code = {'北海道': '010000','青森県': '020000','岩手県': '030000','宮城県': '040000','秋田県': '050000','山形県': '060000',
            '福島県': '070000','栃木県': '080000','群馬県': '090000','茨城県': '100000','埼玉県': '110000','千葉県': '120000',
            '東京都': '130000','神奈川県': '140000','山梨県': '150000','長野県': '160000','新潟県': '170000','富山県': '180000',
            '石川県': '190000','福井県': '200000','静岡県': '210000','岐阜県': '220000','愛知県': '230000','三重県': '240000',
            '滋賀県': '250000','京都府': '260000','大阪府': '270000','兵庫県': '280000','奈良県': '290000','和歌山県': '300000',
            '鳥取県': '310000','島根県': '320000','岡山県': '330000','広島県': '340000','山口県': '350000','徳島県': '360000',
            '香川県': '370000','愛媛県': '380000','高知県': '390000','福岡県': '400000','佐賀県': '410000','長崎県': '420000',
            '熊本県': '430000','大分県': '440000','宮崎県': '450000','鹿児島県': '460000','沖縄県': '470000'}

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

def jaran_search(request):
    form = JaranSearchForm(request.GET or None)
    form.is_valid()
    context = {'form':form}
    if request.method == 'POST':
        data = request.POST
        pref = data['prefecture']
        code = pref_code[pref]
        res = get_api_response(code)
        context['prefecture'] = pref
        context['hotelinfo_list'] = res
    return render(request, 'proto/jaran_search.html',context)

# 指定した都道府県のホテル検索結果を取得
def get_api_response(code):
    url = 'http://jws.jalan.net/APILite/HotelSearch/V1/?key={0}&pref={1}'.format(api_key, code)
    print(url)
    response = requests.get(url)
    response.encoding = response.apparent_encoding
    bs = BeautifulSoup(response.text, 'xml')
    hotel_list = []
    for hotel in bs.find_all('Hotel'):
        name = hotel.HotelName.string
        address = hotel.HotelAddress.string
        hotel_list.append((name,address))
    return hotel_list
