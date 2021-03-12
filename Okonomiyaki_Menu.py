OKONOMIYAKI_MENU = {
    'Aメニュー': {'もち', '明太子', '豚肉'},
    'Bメニュー': {'キムチ', '明太子', '牛肉'},
    'Cメニュー': {'チーズ', '天かす', '牛肉'},
    'Dメニュー': {'もち', 'チーズ', 'イカ'},
}


def output_complement_menu(want_to_eat):

    for menu_name, gu_set in OKONOMIYAKI_MENU.items():
       
        gu_issubset =  want_to_eat <= gu_set # 食べたいものが全て含まれている
     
        gu_intersection = want_to_eat & gu_set # 一部、食べたいものが含まれる
        if gu_issubset:
     
            print('{}に食べたい具が全て揃っています：{}'.format(menu_name, gu_set))
        elif gu_intersection:
           
            print('{}に食べたい具が一部あります：{}'.format(menu_name, gu_intersection))
         
            additional_topping = want_to_eat - gu_set

            print('  追加トッピングは{}です'.format(additional_topping))
        else:
            print('{}には、食べたい具が含まれません'.format(menu_name))


def main():
    want_to_eat = {'明太子', 'もち'}
    print('食べたい具: {}'.format(want_to_eat))

    output_complement_menu(want_to_eat)


if __name__ == '__main__':
    main()
