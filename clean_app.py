# Script to clean app.py
with open('backend/app.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Take only first 775 lines (before the duplicate code)
clean_lines = lines[:775]

# Add chat endpoint
clean_lines.append('\n')
clean_lines.append('@app.route(\'/chat\', methods=[\'POST\'])\n')
clean_lines.append('def chat():\n')
clean_lines.append('    """Chat endpoint untuk career counseling"""\n')
clean_lines.append('    try:\n')
clean_lines.append('        data = request.json\n')
clean_lines.append('        message = data.get(\'message\', \'\')\n')
clean_lines.append('        context = data.get(\'context\')\n')
clean_lines.append('        job_title = context.get(\'jobTitle\') if context else None\n')
clean_lines.append('        \n')
clean_lines.append('        if USE_LLM:\n')
clean_lines.append('            llm_response = generate_chat_response_with_llm(message, job_title)\n')
clean_lines.append('            if llm_response:\n')
clean_lines.append('                return jsonify({\'success\': True, \'response\': llm_response, \'source\': \'ai\'})\n')
clean_lines.append('        \n')
clean_lines.append('        response = "Terima kasih! Saya siap membantu pertanyaan karir Anda. 😊"\n')
clean_lines.append('        return jsonify({\'success\': True, \'response\': response, \'source\': \'fallback\'})\n')
clean_lines.append('    except Exception as e:\n')
clean_lines.append('        return jsonify({\'success\': False, \'error\': str(e)}), 500\n')
clean_lines.append('\n')
clean_lines.append('if __name__ == \'__main__\':\n')
clean_lines.append('    print("Smart Career Recommender API running on http://localhost:5000")\n')
clean_lines.append('    app.run(debug=False, host=\'0.0.0.0\', port=5000, threaded=True, use_reloader=False)\n')

# Write cleaned file
with open('backend/app.py', 'w', encoding='utf-8') as f:
    f.writelines(clean_lines)

print("✅ File app.py cleaned successfully!")
print(f"Total lines: {len(clean_lines)}")
