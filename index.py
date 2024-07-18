import ollama
import click

@click.command()
@click.argument('input', type=str)
@click.option('--file', '-f', is_flag=True, help='Indicates that the input is a file.')
def summarize(input, file):
    """Summarizes text from a file or a direct text input."""
    try:
        if file:
            with open(input, 'r') as f:
                content = f.read()
        else:
            content = input

        my_prompt = f'Please summarize the following text: {content}'
        
        # Making the API call to generate the summary
        response = ollama.generate(model='qwen2:0.5b', prompt=my_prompt)
        
        if 'response' in response:
            actual_response = response['response']
            print(f'\nSummary:\n{actual_response}')
        else:
            print('Error: Unexpected API response format')

    except FileNotFoundError:
        print(f'Error: File "{input}" not found.')
    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == '__main__':
    summarize()
