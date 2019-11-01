import gpt_2_simple as gpt2


def gpt(sentence):
    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess, run_name='run1')
    gpt2.generate(sess)


gpt("hi")



