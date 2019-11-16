import gpt_2_simple as gpt2


def gpt(sentence):
    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess, run_name='run1')
    sent = gpt2.generate(sess, run_name='run1',
              return_as_list=True,
              include_prefix=False,
              prefix=sentence,
              truncate='<|endoftext|>')
    sess.close()

    return sentence





