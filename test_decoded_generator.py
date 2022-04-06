import json
import os

# Return the corresponding text spans of generated rationale(explanation)
def get_spans_generative_split(claim, explanations):
    spans = []
    
    claim_tokens = claim.split()
    claim_tokens_len = len(claim_tokens)
    explanation_tokens = [token for explanation in explanations for token in explanation.split()]
    checkpoint = 0
    is_matched = False
            
    for j, explanation_token in enumerate(explanation_tokens):
        for i, claim_token in enumerate(claim_tokens[checkpoint:]):
            
            if explanation_token == claim_token:
                # Matched
                if is_matched:
                    # Middle of the span
                    spans[-1][1] = checkpoint+i+1
                    checkpoint += i+1
                    break
                else:
                    # Start of the span
                    spans.append([checkpoint+i, checkpoint+i+1])
                    is_matched = True
                    checkpoint += i+1
                    break
            else:
                # Not Matched
                if is_matched:
                    # End of span
                    is_matched = False
                    continue
        
    return spans

if __name__ == '__main__':

    result_dir = 'eraserbenchmark/output'
    test_decoded_file = os.path.join(result_dir, "test_decoded.jsonl")
    
    # Load the prediction result
    with open("predict_results_claimdiff.json", 'r') as json_file:
        preds = json.load(json_file)
    
    decodes = []

    # Decoding
    for i, pred in enumerate(preds):
        annotation_id = pred['annotation_id']
        doc_id = annotation_id[:-1]
        
        rationales = [rationale for rationale in pred['prediction'].split(' explanation: ')[1:]]
        hard_rationale_spans = get_spans_generative_split(pred['claim'], rationales)
        hard_rationale_predictions = [{"start_token": span[0], "end_token": span[1]} for span in hard_rationale_spans]
        
        decode = {
            "annotation_id": annotation_id,
            "rationales": [{
                "docid": doc_id,
                "hard_rationale_predictions": hard_rationale_predictions,
            }]
        }
        
        decodes.append(decode)
    
    # Export test_decoded file as jsonl
    with open(test_decoded_file, 'w') as outfile:
        for entry in decodes:
            json.dump(entry, outfile)
            outfile.write('\n')
