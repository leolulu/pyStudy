r = open(r'E:\Python\PycharmProjects\hellowolrld\file_opreation_directory\测试一.txt', 'r')
a = r.read()
r.close()

a_list = a.split(r'/')

j = 0
for i in a_list:
    w = open('E:\\Python\\PycharmProjects\\hellowolrld\\file_opreation_directory\\' + str(j) + '.txt', 'w')
    w.write(i)
    w.close()

    k = open('E:\\Python\\PycharmProjects\\hellowolrld\\file_opreation_directory\\' + str(j) + '.txt', 'a')
    k.write('\n\\\n')
    k.close()

    j += 1
