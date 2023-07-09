import argparse
import git_logger
import export_sheets

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", help="log pull requests", action="store_true")
    parser.add_argument("-i", help="log issues", action="store_true")
    parser.add_argument("-e", help="log issues", action="store_true")
    parser.add_argument('-t', '--token', type=str, required=True, help='token github account')
    parser.add_argument('-l', '--list', type=str, required=True, help='repos names file')
    parser.add_argument('-o', '--out', type=str, required=True, help='output filename')
    parser.add_argument('--google_token', type=str, required=False, help='Specify path to google token file')
    parser.add_argument('--table_id', type=str, required=False,
                        help='Specify Google sheet document id (can find in url)')
    parser.add_argument('--sheet_id', type=str, required=False,
                        help='Specify title for a sheet in a document in which data will be printed')
    args = parser.parse_args()
    if args.e:
        for action in parser._actions:
            if action.dest == 'google_token':
                action.required = True
            if action.dest == 'table_id':
                action.required = True
            if action.dest == 'sheet_id':
                action.required = True
    return parser.parse_args()


def main():
    args = parse_args()
    token = args.token
    repositories = args.list
    csv_name = args.out

    try:
        client = git_logger.login(token=token)
    except Exception as e:
        print(e)
    else:
        if not args.p and not args.i:
            git_logger.log_commits(client, repositories, csv_name)
            if (args.e):
                export_sheets.write_data_to_table(csv_name, args.google_token, args.table_id, args.sheet_id)
        if args.p:
            git_logger.log_pull_requests(client, repositories, csv_name)
            if (args.e):
                export_sheets.write_data_to_table(csv_name, args.google_token, args.table_id, args.sheet_id)
        if args.i:
            git_logger.log_issues(client, repositories, csv_name)
            if (args.e):
                export_sheets.write_data_to_table(csv_name, args.google_token, args.table_id, args.sheet_id)



if __name__ == '__main__':
    main()
