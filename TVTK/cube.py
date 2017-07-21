from tvtk.api import tvtk
 
# ����һ������������Դ������ͬʱ�����䳤���
s = tvtk.CubeSource(x_length=1.0, y_length=2.0, z_length=3.0)
# ʹ��PolyDataMapper������ת��Ϊͼ������
m = tvtk.PolyDataMapper(input_connection=s.output_port)
# ����һ��Actor
a = tvtk.Actor(mapper=m)
# ����һ��Renderer����Actor��ӽ�ȥ
r = tvtk.Renderer(background=(0, 0, 0))
r.add_actor(a)
# ����һ��RenderWindow(����)����Renderer��ӽ�ȥ
w = tvtk.RenderWindow(size=(300,300))
w.add_renderer(r)
# ����һ��RenderWindowInteractor�����ڵĽ�������)
i = tvtk.RenderWindowInteractor(render_window=w)
# ��������
i.initialize()
i.start()