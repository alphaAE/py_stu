if __name__ == '__main__':

    with open("./DataSource/comm.txt", 'r', encoding='utf8') as file:
        outfile = open("./DataSource/comm2.txt", 'w', encoding='utf8')
        words = file.readlines()
        for word in words:

            content = '| ' + word[:-1] + ' |' + word[-1]
            index = word.rfind('-')
            contentList = list(content)
            contentList[index + 2] = '|'
            rul = ''.join(contentList)
            print(rul)

            outfile.writelines(rul)

        outfile.close()
