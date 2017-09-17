任务=进程Process(多进程-单进程；父进程-子进程)--子任务=线程Thread(多线程-单线程；主线程-子线程)--协程coroutine(微线程，函数)
多任务即多进程执行方式(顺序执行—交替执行—同步执行(多核CPU才能实现))
多任务=多进程=多线程
多任务的实现(多进程模式--多线程模式--多进程+多线程模式)
多线程的执行方式和多进程是一样的
高级语言的一条语句在CPU执行时是若干条语句
'进程和线程'
	概念
		任务=进程(Process)—单进程—多进程(multiprocessing)--线程(Thread)—单线程—多线程(multi threading)
		单核CPU--多核CPU
		多任务执行方式(顺序执行—交替执行—同步执行)
			单核CPU是怎么执行多任务的呢？-- 交替执行
				答案就是操作系统轮流让各个任务交替执行，任务1执行0.01秒，切换到任务2，任务2执行0.01秒，再切换到任务3，
				执行0.01秒……这样反复执行下去。表面上看，每个任务都是交替执行的，但是，由于CPU的执行速度实在是太快了，
				我们感觉就像所有任务都在同时执行一样。
			真正的并行执行多任务只能在多核CPU上实现
				但是，由于任务数量远远多于CPU的核心数量，所以，操作系统也会自动把很多任务轮流调度到每个核心上执行。
				对于操作系统来说，一个任务就是一个进程(Process)，比如打开一个浏览器就是启动一个浏览器进程，打开一个记事本
				就启动了一个记事本进程，打开两个记事本就启动了两个记事本进程，打开一个Word就启动了一个Word进程。
				有些进程还不止同时干一件事，比如Word，它可以同时进行打字、拼写检查、打印等事情。在一个进程内部，要同时干多件
				事，就需要同时运行多个“子任务”，我们把进程内的这些“子任务”称为线程(Thread)。
				由于每个进程至少要干一件事，所以，一个进程至少有一个线程。当然，像Word这种复杂的进程可以有多个线程，多个
				线程可以同时执行，多线程的执行方式和多进程是一样的，也是由操作系统在多个线程之间快速切换，让每个线程都短暂地
				交替运行，看起来就像同时执行一样。当然，真正地同时执行多线程需要多核CPU才可能实现。
		多任务的实现有3种方式：
				•	多进程模式；
				•	多线程模式；
				•	多进程+多线程模式。
				同时执行多个任务通常各个任务之间并不是没有关联的，而是需要相互通信和协调，有时，任务1必须暂停等待任务2
				完成后才能继续执行，有时，任务3和任务4又不能同时执行，所以，多进程和多线程的程序的复杂度要远远高于我们前
				面写的单进程单线程的程序。
				因为复杂度高，调试困难，所以，不是迫不得已，我们也不想编写多任务。但是，有很多时候，没有多任务还真不行。
				想想在电脑上看电影，就必须由一个线程播放视频，另一个线程播放音频，否则，单线程实现的话就只能先把视频播放
				完再播放音频，或者先把音频播放完再播放视频，这显然是不行的。
				Python既支持多进程，又支持多线程，我们会讨论如何编写这两种多任务程序。
		小结
				线程是最小的执行单元，而进程由至少一个线程组成。如何调度进程和线程，完全由操作系统决定，程序自己不能
				决定什么时候执行，执行多长时间。
				多进程和多线程的程序涉及到同步、数据共享的问题，编写起来更复杂。
	多进程
		fork()系统调用--Unix/Linux操作系统提供--支持多进程
			了解操作系统的相关知识
					Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。普通的函数调用，调用一次，返回一次，
					但是fork()调用一次，返回两次，因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），
					然后，分别在父进程和子进程内返回。
					子进程永远返回0，而父进程返回子进程的ID。这样做的理由是，一个父进程可以fork出很多子进程，所以，
					父进程要记下每个子进程的ID，而子进程只需要调用getpid()就可以拿到父进程的ID。
			Python的os模块封装了常见的系统调用，其中就包括fork，可以创建子进程：
					import os					
					print('Process (%s) start...' % os.getpid())
					# Only works on Unix/Linux/Mac:
					pid = os.fork()
					if pid == 0:
					    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
					else:
					    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
					    #  两个参数分别是父进程，子进程的pid。
					运行结果如下：
					Process (876) start...
					I (876) just created a child process (877).
					I am child process (877) and my parent is 876.
			Windows没有fork调用，上面的代码在Windows上无法运行				
		multiprocessing模块--跨平台--支持多进程
			Process类--创建子进程对象
				启动一个子进程并等待其结束：
					from multiprocessing import Process
					import os					
					# 子进程要执行的代码
					def run_proc(name):
					    print('Run child process %s (%s)...' % (name, os.getpid()))					
					if __name__=='__main__':
					    print('Parent process %s.' % os.getpid())
					    p = Process(target=run_proc, args=('test',))
					    print('Child process will start.')
					    p.start()
					    p.join()
					    print('Child process end.')
				执行结果如下：
					Parent process 928.
					Child Process will start.
					Run child process test (929)...
					Child Process end.
				创建子进程时，只需要传入一个执行函数和函数的参数
				创建一个Process实例，用start()方法启动
				join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
			Pool--进程池批量创建子进程
				如果要启动大量的子进程，可以用进程池的方式批量创建子进程：
					from multiprocessing import Pool
					import os, time, random					
					def long_time_task(name):
					    print('Run task %s (%s)...' % (name, os.getpid()))
					    start = time.time()
					    time.sleep(random.random() * 3)
					    end = time.time()
					    print('Task %s runs %0.2f seconds.' % (name, (end - start)))					
					if __name__=='__main__':
					    print('Parent process %s.' % os.getpid())
					    p = Pool(4)
					    for i in range(5):
					        p.apply_async(long_time_task, args=(i,))
					    print('Waiting for all subprocesses done...')
					    p.close()
					    p.join()
					    print('All subprocesses done.')
				执行结果如下：
					Parent process 669.
					Waiting for all subprocesses done...
					Run task 0 (671)...
					Run task 1 (672)...
					Run task 2 (673)...
					Run task 3 (674)...
					Task 2 runs 0.14 seconds.
					Run task 4 (673)...
					Task 1 runs 0.27 seconds.
					Task 3 runs 0.86 seconds.
					Task 0 runs 1.41 seconds.
					Task 4 runs 1.91 seconds.
					All subprocesses done.
				代码解读：
					对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。
					请注意输出的结果，task 0，1，2，3是立刻执行的，而task 4要等待前面某个task完成后才执行，这是因为Pool的默认大小在我的电脑上是4，
					因此，最多同时执行4个进程。这是Pool有意设计的限制，并不是操作系统的限制。如果改成：
					p = Pool(5)
					就可以同时跑5个进程。
					由于Pool的默认大小是CPU的核数，如果你不幸拥有8核CPU，你要提交至少9个子进程才能看到上面的等待效果。

					apply_async，是非阻塞的，意思就是主函数会自个执行自个，不搭理子进程的执行，这也是为什么第二行会在子进程返回结果的上方，
					apply是阻塞的，阻塞就是主函数后面的部分要等待子进程结束后才执行，将主函数堵住了嘛，后面这括号里面的一个是函数，
					一个是函数的参数

					多进程并发执行能够充分利用计算机的硬件。提高运行速度。讲讲我现在对进程池的理解：

					进程池的实例在定义的时候就确定了包含多少个进程任务：
					p=Pool(4)
					表示进程池中有四个任务，计算机将会为进程池预分配4个pid
					for task in range(5):
					会先把前四个进程进行并发执行，有一个进程结束的时候立即开始第5个进程。但是值得注意的是，第5个进程并不会分配新的pid。
					如果在创建Pool实例的时候不写参数：
					p=Pool()
					则参数默认为当前计算机的核数。
		subprocess模块--启动一个子进程--控制其输入和输出
			subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。很多时候，子进程并不是自身，而是一个外部进程
				下面的例子演示了如何在Python代码中运行命令nslookup www.python.org，这和命令行直接运行的效果是一样的：
					import subprocess					
					print('$ nslookup www.python.org')
					r = subprocess.call(['nslookup', 'www.python.org'])
					print('Exit code:', r)
				运行结果：
					$ nslookup www.python.org
					Server:        192.168.19.4
					Address:    192.168.19.4#53					
					Non-authoritative answer:
					www.python.org    canonical name = python.map.fastly.net.
					Name:    python.map.fastly.net
					Address: 199.27.79.223					
					Exit code: 0
				如果子进程还需要输入，则可以通过 communicate()方法输入：
					import subprocess					
					print('$ nslookup')
					p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
					output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
					print(output.decode('utf-8'))
					print('Exit code:', p.returncode)
					上面的代码相当于在命令行执行命令nslookup，然后手动输入：
					set q=mx
					python.org
					exit
					运行结果如下：
					$ nslookup
					Server:        192.168.19.4
					Address:    192.168.19.4#53					
					Non-authoritative answer:
					python.org    mail exchanger = 50 mail.python.org.					
					Authoritative answers can be found from:
					mail.python.org    internet address = 82.94.164.166
					mail.python.org    has AAAA address 2001:888:2000:d::a6					
					Exit code: 0
		进程间通信--multiprocessing模块--Queue、Pipes
			操作系统提供很多机制来实现进程间的通信。Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。
				我们以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据：
					from multiprocessing import Process, Queue
					import os, time, random					
					# 写数据进程执行的代码:
					def write(q):
					    print('Process to write: %s' % os.getpid())
					    for value in ['A', 'B', 'C']:
					        print('Put %s to queue...' % value)
					        q.put(value)
					        time.sleep(random.random())					
					# 读数据进程执行的代码:
					def read(q):
					    print('Process to read: %s' % os.getpid())
					    while True:
					        value = q.get(True)
					        print('Get %s from queue.' % value)					
					if __name__=='__main__':
					    # 父进程创建Queue，并传给各个子进程：
					    q = Queue()
					    pw = Process(target=write, args=(q,))
					    pr = Process(target=read, args=(q,))
					    # 启动子进程pw，写入:
					    pw.start()
					    # 启动子进程pr，读取:
					    pr.start()
					    # 等待pw结束:
					    pw.join()
					    # pr进程里是死循环，无法等待其结束，只能强行终止:
					    pr.terminate()
				运行结果如下：
					Process to write: 50563
					Put A to queue...
					Process to read: 50564
					Get A from queue.
					Put B to queue...
					Get B from queue.
					Put C to queue...
					Get C from queue.		
		小结
			在Unix/Linux下，multiprocessing模块封装了fork()调用，使我们不需要关注fork()的细节。由于Windows没有fork调用，
			因此，multiprocessing需要“模拟”出fork的效果，父进程所有Python对象都必须通过pickle序列化再传到子进程去，所以，
			如果multiprocessing在Windows下调用失败了，要先考虑是不是pickle失败了。	
			在Unix/Linux下，可以使用fork()调用实现多进程。要实现跨平台的多进程，可以使用multiprocessing模块。
			进程间通信是通过Queue、Pipes等实现的。
		参考源码
			do_folk.py
			multi_processing.py
			pooled_processing.py
			do_subprocess.py
			do_queue.py
	多线程 -- 完成多任务
		_thread 低级模块-封装
		threading 高级模块
			启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行：
			运行代码
					import time, threading					
					# 新线程执行的代码:
					def loop():
					    print('thread %s is running...' % threading.current_thread().name)
					    n = 0
					    while n < 5:
					        n = n + 1
					        print('thread %s >>> %s' % (threading.current_thread().name, n))
					        time.sleep(1)
					    print('thread %s ended.' % threading.current_thread().name)					
					print('thread %s is running...' % threading.current_thread().name)
					t = threading.Thread(target=loop, name='LoopThread')
					t.start()
					t.join()
					# join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
					print('thread %s ended.' % threading.current_thread().name)
			执行结果如下：
					thread MainThread is running...
					thread LoopThread is running...
					thread LoopThread >>> 1
					thread LoopThread >>> 2
					thread LoopThread >>> 3
					thread LoopThread >>> 4
					thread LoopThread >>> 5
					thread LoopThread ended.
					thread MainThread ended.
			代码解读
            				由于任何进程默认就会启动一个线程，我们把该线程称为主线程，主线程又可以启动新的线程
            				Python的threading模块有个 current_thread()函数，它永远返回当前线程的实例。主线程实例的
            				名字叫MainThread，
            				子线程的名字在创建时指定，我们用LoopThread命名子线程。名字仅仅在打印时用来显示，完全没有
            				其他意义，如果不起名字Python就自动给线程命名为Thread-1，Thread-2……
		线程锁--threading.Lock()--获取锁--释放锁
			多线程和多进程最大的不同--变量是否共享
				多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响
				而多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改
				因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。
			例
				import time, threading					
				# 假定这是你的银行存款:
				balance = 0					
				def change_it(n):
				    # 先存后取，结果应该为0:
				    global balance
				    balance = balance + n
				    balance = balance - n					
				def run_thread(n):
				    for i in range(100000):
				        change_it(n)					
				t1 = threading.Thread(target=run_thread, args=(5,))
				t2 = threading.Thread(target=run_thread, args=(8,))
				t1.start()
				t2.start()
				t1.join()
				t2.join()
				print(balance)
			代码解读
				我们定义了一个共享变量balance，初始值为0，并且启动两个线程，先存后取，理论上结果应该为0，但是，由于线程的调度是由
				操作系统决定的，当t1、t2交替执行时，只要循环次数足够多，balance的结果就不一定是0了。

				原因--是因为高级语言的一条语句在CPU执行时是若干条语句，即使一个简单的计算：
				balance = balance + n
				也分两步：
				1.	计算balance + n，存入临时变量中；
				2.	将临时变量的值赋给balance。
				也就是可以看成：
				x = balance + n
				balance = x
				由于x是局部变量，两个线程各自都有自己的x，当代码正常执行时：
				初始值 balance = 0					
				t1: x1 = balance + 5 # x1 = 0 + 5 = 5
				t1: balance = x1     # balance = 5
				t1: x1 = balance - 5 # x1 = 5 - 5 = 0
				t1: balance = x1     # balance = 0					
				t2: x2 = balance + 8 # x2 = 0 + 8 = 8
				t2: balance = x2     # balance = 8
				t2: x2 = balance - 8 # x2 = 8 - 8 = 0
				t2: balance = x2     # balance = 0					
				结果 balance = 0
				但是t1和t2是交替运行的，如果操作系统以下面的顺序执行t1、t2：
				初始值 balance = 0					
				t1: x1 = balance + 5  # x1 = 0 + 5 = 5					
				t2: x2 = balance + 8  # x2 = 0 + 8 = 8
				t2: balance = x2      # balance = 8					
				t1: balance = x1      # balance = 5
				t1: x1 = balance - 5  # x1 = 5 - 5 = 0
				t1: balance = x1      # balance = 0					
				t2: x2 = balance - 8  # x2 = 0 - 8 = -8
				t2: balance = x2   # balance = -8					
				结果 balance = -8
				究其原因，是因为修改balance需要多条语句，而执行这几条语句时，线程可能中断，从而导致多个线程把同一个对象的内容改乱了。
				两个线程同时一存一取，就可能导致余额不对，你肯定不希望你的银行存款莫名其妙地变成了负数，所以，我们必须确保一个线程在
				修改balance的时候，别的线程一定不能改。
		
				如果我们要确保balance计算正确，就要给change_it()上一把锁，当某个线程开始执行change_it()时，我们说，该线程因为获得了锁，
				因此其他线程不能同时执行change_it()，只能等待，直到锁被释放后，获得该锁以后才能改。由于锁只有一个，无论多少线程，同一
				时刻最多只有一个线程持有该锁，所以，不会造成修改的冲突。创建一个锁就是通过threading.Lock()来实现：
				balance = 0
				lock = threading.Lock()					
				def run_thread(n):
				    for i in range(100000):
				        # 先要获取锁:
				        lock.acquire()
				        try:
				            # 放心地改吧:
				            change_it(n)
				        finally:
				            # 改完了一定要释放锁:
				            lock.release()
				当多个线程同时执行lock.acquire()时，只有一个线程能成功地获取锁，然后继续执行代码，其他线程就继续等待直到获得锁为止。
				获得锁的线程用完后一定要释放锁，否则那些苦苦等待锁的线程将永远等待下去，成为死线程。所以我们用try...finally来确保锁一定
				会被释放。
				锁的好处就是确保了某段关键代码只能由一个线程从头到尾完整地执行，坏处当然也很多，首先是阻止了多线程并发执行，包含锁的
				某段代码实际上只能以单线程模式执行，效率就大大地下降了。其次，由于可以存在多个锁，不同的线程持有不同的锁，并试图获取
				对方持有的锁时，可能会造成死锁，导致多个线程全部挂起，既不能执行，也无法结束，只能靠操作系统强制终止。
	ThreadLocal--解决参数在一个线程中各个函数之间相互传递的问题

		在多线程环境下，每个线程都有自己的数据。一个线程使用自己的局部变量比使用全局变量好，因为局部变量只有线程自己能看见，不会影响其他线程，
		而全局变量的修改必须加锁。				

		但是局部变量也有问题，就是在函数调用的时候，传递起来很麻烦：

				def process_student(name):
				    std = Student(name)
				    # std是局部变量，但是每个函数都要用它，因此必须传进去：
				    do_task_1(std)
				    do_task_2(std)				

				def do_task_1(std):
				    do_subtask_1(std)
				    do_subtask_2(std)				

				def do_task_2(std):
				    do_subtask_2(std)
				    do_subtask_2(std)
				每个函数一层一层调用都这么传参数那还得了？用全局变量？也不行，因为每个线程处理不同的Student对象，不能共享。				

		如果用一个全局dict存放所有的Student对象，然后以thread自身作为key获得线程对应的Student对象如何？

				global_dict = {}				

				def std_thread(name):
				    std = Student(name)
				    # 把std放到全局变量global_dict中：
				    global_dict[threading.current_thread()] = std
				    do_task_1()
				    do_task_2()				

				def do_task_1():
				    # 不传入std，而是根据当前线程查找：
				    std = global_dict[threading.current_thread()]
				    ...				

				def do_task_2():
				    # 任何函数都可以查找出当前线程的std变量：
				    std = global_dict[threading.current_thread()]
				    ...
				这种方式理论上是可行的，它最大的优点是消除了std对象在每层函数中的传递问题，但是，每个函数获取std的代码有点丑。				

				有没有更简单的方式？				

		ThreadLocal应运而生，不用查找dict，ThreadLocal帮你自动做这件事：
			代码如下
				import threading				

				# 创建全局ThreadLocal对象:
				local_school = threading.local()				

				def process_student():
				    # 获取当前线程关联的student:
				    std = local_school.student
				    print('Hello, %s (in %s)' % (std, threading.current_thread().name))				

				def process_thread(name):
				    # 绑定ThreadLocal的student:
				    local_school.student = name
				    process_student()				

				t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
				t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
				t1.start()
				t2.start()
				t1.join()
				t2.join()
			执行结果：

				Hello, Alice (in Thread-A)
				Hello, Bob (in Thread-B)
			代码解读
				全局变量local_school就是一个ThreadLocal对象，每个Thread对它都可以读写student属性，但互不影响。你可以把local_school看成全局变量，
				但每个属性如local_school.student都是线程的局部变量，可以任意读写而互不干扰，也不用管理锁的问题，ThreadLocal内部会处理。				

				可以理解为全局变量local_school是一个dict，不但可以用local_school.student，还可以绑定其他变量，如local_school.teacher等等。				

				ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，这样一个线程的所有调用到的处理函数都可以非常
				方便地访问这些资源。				

			小结

				一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。ThreadLocal解决了参数在一个线程中各个函数
				之间互相传递的问题。				

			参考源码

				use_threadlocal.py
	多核CPU
			如果写一个死循环的话，会出现什么情况呢？
				打开Mac OS X的Activity Monitor，或者Windows的Task Manager，都可以监控某个进程的CPU使用率。
				我们可以监控到一个死循环线程会100%占用一个CPU。
				如果有两个死循环线程，在多核CPU中，可以监控到会占用200%的CPU，也就是占用两个CPU核心。
				要想把N核CPU的核心全部跑满，就必须启动N个死循环线程。
			试试用Python写个死循环：
				import threading, multiprocessing					
				def loop():
				    x = 0
				    while True:
				        x = x ^ 1					
				for i in range(multiprocessing.cpu_count()):
				    t = threading.Thread(target=loop)
				    t.start()
				启动与CPU核心数量相同的N个线程，在4核CPU上可以监控到CPU占用率仅有102%，也就是仅使用了一核。
			但是用C、C++或Java来改写相同的死循环，直接可以把全部核心跑满，
			为什么Python不行呢？--GIL锁
				因为Python的线程虽然是真正的线程，但解释器执行代码时，有一个GIL锁：Global Interpreter Lock，任何Python线程
				执行前，必须先获得GIL锁，然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。这个GIL全局
				锁实际上把所有线程的执行代码都给上了锁，所以，多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，
				也只能用到1个核。
				GIL是Python解释器设计的历史遗留问题，通常我们用的解释器是官方实现的CPython，要真正利用多核，除非重写一个
				不带GIL的解释器。
				所以，在Python中，可以使用多线程，但不要指望能有效利用多核。如果一定要通过多线程利用多核，那只能通过C扩展来
				实现，不过这样就失去了Python简单易用的特点。
				不过，也不用过于担心，Python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务。多个Python进程有
				各自独立的GIL锁，互不影响。
			小结
				多线程编程，模型复杂，容易发生冲突，必须用锁加以隔离，同时，又要小心死锁的发生。
				Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。多线程的并发在Python中就是一个美丽的梦。
			参考源码
				multi_threading.py
				do_lock.py
'进程 vs. 线程'--实现多任务最常用的两种方式
	优缺点
		实现多任务，通常我们会设计Master-Worker模式，Master负责分配任务，Worker负责执行任务
			通常是一个Master，多个Worker
				多进程实现Master-Worker，主进程就是Master，其他进程就是Worker。
				多线程实现Master-Worker，主线程就是Master，其他线程就是Worker。
		多进程模式最大的优点就是稳定性高
			
			因为一个子进程崩溃了，不会影响主进程和其他子进程。（当然主进程挂了所有进程就全挂了，但是Master进程只负责分配任务，挂掉的概率低）
		多进程模式的缺点是创建进程的代价大
		多线程模式通常比多进程快一点，但是也快不到哪去
		多线程模式致命的缺点就是任何一个线程挂掉都可能直接造成整个进程崩溃
			因为所有线程共享进程的内存。在Windows上，如果一个线程执行的代码出了问题，你经常可以看到这样的提示：“该程序执行了非法操作，
			即将关闭”，其实往往是某个线程出了问题，但是操作系统会强制结束整个进程。
					
		线程切换
		无论是多进程还是多线程，只要数量一多，效率肯定上不去
		任务类型(计算密集型 vs. IO密集型)
			计算密集型任务--要进行大量的计算，消耗CPU资源--可以有效利用多核
					比如计算圆周率、对视频进行高清解码等等，全靠CPU的运算能力。
					这种计算密集型任务虽然也可以用多任务完成，但是任务越多，花在任务切换的时间就越多，CPU执行任务的效率就越低，所以，
					要最高效地利用CPU，计算密集型任务同时进行的数量应当等于CPU的核心数。
					计算密集型任务由于主要消耗CPU资源，因此，代码运行效率至关重要。Python这样的脚本语言运行效率很低，完全不适合计算
					密集型任务。对于计算密集型任务，最好用C语言编写。
			IO密集型任务--大部分时间在等待IO操作完成, CPU消耗很少--任务越多，CPU效率越高
				涉及到网络、磁盘IO的任务都是IO密集型任务（因为IO的速度远远低于CPU和内存的速度）。常见的大部分任务都是IO密集型任务
					IO密集型任务执行期间，99%的时间都花在IO上，花在CPU上的时间很少，因此，用运行速度极快的C语言替换用Python这样运行
					速度极低的脚本语言，完全无法提升运行效率。对于IO密集型任务，最合适的语言就是开发效率最高（代码量最少）的语言，
					脚本语言是首选，C语言最差。
		异步IO--事件驱动模型--单进程单线程模型执行多任务--对应到Python语言，单进程的异步编程模型称为协程
'分布式进程'--分布式多进程程序	-- 实现多任务分布
	在Thread和Process中，应当优选Process，因为Process更稳定，而且，Process可以分布到多台机器上，而Thread最多只能分布到同一台机器的多个CPU上。
		multiprocessing模块--支持把多进程分布到多台机器上执行任务
			一个服务进程可以作为调度者，将任务分布到其他多个进程中，依靠网络通信。由于managers模块封装很好，不必了解网络通信的细节，
			就可以很容易地编写分布式多进程程序。
		举个例子
			如果我们已经有一个通过Queue通信的多进程程序在同一台机器上运行，现在，由于处理任务的进程任务繁重，希望把发送
			任务的进程和处理任务的进程分布到两台机器上。怎么用分布式进程实现？
			原有的Queue可以继续使用，但是，通过managers模块把Queue通过网络暴露出去，就可以让其他机器的进程访问Queue了。
				我们先看服务进程，服务进程负责启动Queue，把Queue注册到网络上，然后往Queue里面写入任务：
					# task_master.py					

					import random, time, queue
					from multiprocessing.managers import BaseManager					

					# 发送任务的队列:
					task_queue = queue.Queue()
					# 接收结果的队列:
					result_queue = queue.Queue()					

					# 从BaseManager继承的QueueManager:
					class QueueManager(BaseManager):
					    pass					

					# 把两个Queue都注册到网络上, callable参数关联了Queue对象:
					QueueManager.register('get_task_queue', callable=lambda: task_queue)
					QueueManager.register('get_result_queue', callable=lambda: result_queue)
					# 绑定端口5000, 设置验证码'abc':
					manager = QueueManager(address=('', 5000), authkey=b'abc')
					# 启动Queue:
					manager.start()
					# 获得通过网络访问的Queue对象:
					task = manager.get_task_queue()
					result = manager.get_result_queue()
					# 放几个任务进去:
					for i in range(10):
					    n = random.randint(0, 10000)
					    print('Put task %d...' % n)
					    task.put(n)
					# 从result队列读取结果:
					print('Try get results...')
					for i in range(10):
					    r = result.get(timeout=10)
					    print('Result: %s' % r)
					# 关闭:
					manager.shutdown()
					print('master exit.')
					请注意，当我们在一台机器上写多进程程序时，创建的Queue可以直接拿来用，但是，在分布式多进程环境下，添加任务到Queue不
					可以直接对原始的task_queue进行操作，那样就绕过了QueueManager的封装，必须通过manager.get_task_queue()获得的Queue
					接口添加。
				然后，在另一台机器上启动任务进程（本机上启动也可以）：
					# task_worker.py					

					import time, sys, queue
					from multiprocessing.managers import BaseManager					

					# 创建类似的QueueManager:
					class QueueManager(BaseManager):
					    pass					

					# 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字:
					QueueManager.register('get_task_queue')
					QueueManager.register('get_result_queue')					

					# 连接到服务器，也就是运行task_master.py的机器:
					server_addr = '127.0.0.1'
					print('Connect to server %s...' % server_addr)
					# 端口和验证码注意保持与task_master.py设置的完全一致:
					m = QueueManager(address=(server_addr, 5000), authkey=b'abc')
					# 从网络连接:
					m.connect()
					# 获取Queue的对象:
					task = m.get_task_queue()
					result = m.get_result_queue()
					# 从task队列取任务,并把结果写入result队列:
					for i in range(10):
					    try:
					        n = task.get(timeout=1)
					        print('run task %d * %d...' % (n, n))
					        r = '%d * %d = %d' % (n, n, n*n)
					        time.sleep(1)
					        result.put(r)
					    except Queue.Empty:
					        print('task queue is empty.')
					# 处理结束:
					print('worker exit.')
				任务进程要通过网络连接到服务进程，所以要指定服务进程的IP。
				现在，可以试试分布式进程的工作效果了。先启动task_master.py服务进程：
					$ python3 task_master.py 
					Put task 3411...
					Put task 1605...
					Put task 1398...
					Put task 4729...
					Put task 5300...
					Put task 7471...
					Put task 68...
					Put task 4219...
					Put task 339...
					Put task 7866...
					Try get results...
					task_master.py进程发送完任务后，开始等待result队列的结果。现在启动task_worker.py进程：
					$ python3 task_worker.py
					Connect to server 127.0.0.1...
					run task 3411 * 3411...
					run task 1605 * 1605...
					run task 1398 * 1398...
					run task 4729 * 4729...
					run task 5300 * 5300...
					run task 7471 * 7471...
					run task 68 * 68...
					run task 4219 * 4219...
					run task 339 * 339...
					run task 7866 * 7866...
					worker exit.
					task_worker.py进程结束，在task_master.py进程中会继续打印出结果：
					Result: 3411 * 3411 = 11634921
					Result: 1605 * 1605 = 2576025
					Result: 1398 * 1398 = 1954404
					Result: 4729 * 4729 = 22363441
					Result: 5300 * 5300 = 28090000
					Result: 7471 * 7471 = 55815841
					Result: 68 * 68 = 4624
					Result: 4219 * 4219 = 17799961
					Result: 339 * 339 = 114921
					Result: 7866 * 7866 = 61873956
					这个简单的Master/Worker模型有什么用？其实这就是一个简单但真正的分布式计算，把代码稍加改造，启动多个worker，就可以把任务
					分布到几台甚至几十台机器上，比如把计算n*n的代码换成发送邮件，就实现了邮件队列的异步发送。
					Queue对象存储在哪？注意到task_worker.py中根本没有创建Queue的代码，所以，Queue对象存储在task_master.py进程中：
					 
					而Queue之所以能通过网络访问，就是通过QueueManager实现的。由于QueueManager管理的不止一个Queue，所以，要给每个
					Queue的网络调用接口起个名字，比如get_task_queue。
					authkey有什么用？这是为了保证两台机器正常通信，不被其他机器恶意干扰。如果task_worker.py的authkey和task_master.py的authkey
					不一致，肯定连接不上。
	小结
					Python的分布式进程接口简单，封装良好，适合需要把繁重任务分布到多台机器的环境下。
					注意Queue的作用是用来传递任务和接收结果，每个任务的描述数据量要尽量小。比如发送一个处理日志文件的任务，就不要发送几百兆
					的日志文件本身，而是发送日志文件存放的完整路径，由Worker进程再去共享的磁盘上读取文件。
	参考源码
					task_master.py
					task_worker.py
'异步IO' -- 解决CPU和IO之间的速度不匹配--消息循环 -- CPU不等待IO执行的结果，执行其他任务，当IO返回结果时，再通知CPU进行处理
	多线程和多进程只是解决这一问题的一种方法
	另一种方法是异步IO --消息循环-- CPU不等待IO执行的结果，执行其他任务，当IO返回结果时，再通知CPU进行处理
			
		异步IO模型需要一个消息循环，在消息循环中，主线程不断地重复“读取消息-处理消息”这一过程：
				loop = get_event_loop()
				while True:
				    event = loop.get_event()
				    process_event(event)
				
		消息模型是如何解决同步IO必须等待IO操作这一问题的呢？
			当遇到IO操作时，代码只负责发出IO请求，不等待IO结果，然后直接结束本轮消息处理，进入下一轮消息处理过程。当IO操作完成后，将收到一条
			“IO完成”的消息，处理该消息时就可以直接获取IO操作结果。
'协程' – coroutine (co+routine) or 微线程--一个线程执行--执行过程中断--通过generator实现
	区别线程、协程（微线程）、子程序（函数），协程调用和函数调用
		协程()-微线程--一个线程执行--执行过程中断--通过generator实现
			又称微线程，纤程。英文名Coroutine。协程看上去也是子程序，但执行过程中，在子程序内部可中断，然后转而执行别的子程序，在适当的
			时候再返回来接着执行。协程的特点在于是一个线程执行。Python对协程的支持是通过generator实现的。Python的yield不但可以返回一个值，
			它还可以接收调用者发出的参数
		子程序(函数)--层级调用--调用是通过栈实现--“子程序就是协程的一种特例-不中断”
			或者称为函数，在所有语言中都是层级调用，比如A调用B，B在执行过程中又调用了C，C执行完毕返回，B执行完毕返回，最后是A执行完毕。
			所以子程序（函数）调用是通过栈实现的
		线程()--一个线程就是执行一个（或多个）子程序
		子程序调用()--总是一个入口，一次返回，调用顺序是明确的。函数的执行方式是调用－返回，可以嵌套
		协程调用()--和子程序不同，在一个子程序中中断，去执行其他子程序，通过generator实现，有点类似CPU的中断。
			协程的执行方式是执行－遇到IO中断－继续执行，关键是中断的时候线程去执行其他可以执行的协程去了


	在学习异步IO模型前，我们先来了解协程。
		注意，在一个子程序中中断，去执行其他子程序，不是函数调用，有点类似CPU的中断。比如子程序A、B：
					def A():
					    print('1')
					    print('2')
					    print('3')					

					def B():
					    print('x')
					    print('y')
					    print('z')
			假设由协程执行，在执行A的过程中，可以随时中断，去执行B，B也可能在执行过程中中断再去执行A，结果可能是：
					1
					2
					x
					y
					3
					z
			但是在A中是没有调用B的，所以协程的调用比函数调用理解起来要难一些。
		和多线程比，协程有何优势？
			优势1 协程执行效率极高。因为子程序切换不是线程切换，而是由程序自身控制，故没有线程切换的开销，和多线程比，线程数量越多，协程优势就越明显。
			优势2 不需要多线程的'锁机制'，因为只有一个线程，也不存在同时写变量冲突，在协程中控制共享资源不加锁，只需要判断状态就好
		因为协程是一个线程执行，那怎么利用多核CPU呢？
			最简单的方法是多进程+协程，既充分利用多核，又充分发挥协程的高效率，可获得极高的性能。
	Python对协程的支持是通过generator实现的。
			在generator中，我们不但可以通过for循环来迭代，还可以不断调用next()函数获取由yield语句返回的下一个值。
			但是Python的yield不但可以返回一个值，它还可以接收调用者发出的参数。
			来看例子：
				传统的生产者-消费者模型是一个线程写消息，一个线程取消息，通过锁机制控制队列和等待，但一不小心就可能死锁。
				如果改用协程，生产者生产消息后，直接通过yield跳转到消费者开始执行，待消费者执行完毕后，切换回生产者继续生产，效率极高：
					def consumer():
					    r = ''
					    while True:
					        n = yield r
					        if not n:
					            return
					        print('[CONSUMER] Consuming %s...' % n)
					        r = '200 OK'					

					def produce(c):
					    c.send(None)
					    n = 0
					    while n < 5:
					        n = n + 1
					        print('[PRODUCER] Producing %s...' % n)
					        r = c.send(n)
					        print('[PRODUCER] Consumer return: %s' % r)
					    c.close()					

					c = consumer()
					produce(c)
					可能有坑！修改如下：
					def consumer():
					    r = ''
					    while True:
					        consumer_n = yield r
					        if not n:
					            return
					        print('[CONSUMER] Consuming %s...' % consumer_n)
					        r = '200 OK'					

					def produce(c):
					    c.send(None) # 调用c.send(None)启动生成器
					    n = 0
					    while n < 5:
					        n = n + 1
					        print('[PRODUCER] Producing %s...' % n)
					        produce_r = c.send(n) 
					        print('[PRODUCER] Consumer return: %s' % produce_r)
					    c.close()					

					c = consumer()
					produce(c)
				执行结果：
					[PRODUCER] Producing 1...
					[CONSUMER] Consuming 1...
					[PRODUCER] Consumer return: 200 OK
					[PRODUCER] Producing 2...
					[CONSUMER] Consuming 2...
					[PRODUCER] Consumer return: 200 OK
					[PRODUCER] Producing 3...
					[CONSUMER] Consuming 3...
					[PRODUCER] Consumer return: 200 OK
					[PRODUCER] Producing 4...
					[CONSUMER] Consuming 4...
					[PRODUCER] Consumer return: 200 OK
					[PRODUCER] Producing 5...
					[CONSUMER] Consuming 5...
					[PRODUCER] Consumer return: 200 OK
				代码解读
					无论是send还是next，都会从上次执行的yield的下一行开始执行，并且执行到下一个yield，这个下一个yield这行是要执行的，但是
					执行完就停住
					yield r是一个表达式，通过send(msg)被赋值， 而send(msg)是有返回值的，返回值为：下一个 yield r 表达式中的 r
					注意到consumer函数是一个generator，把一个consumer传入produce后：
					1.	首先调用c.send(None)启动生成器；
					2.	然后，一旦生产了东西，通过c.send(n)切换到consumer执行；
					3.	consumer通过yield拿到消息，处理，又通过yield把结果传回；
					4.	produce拿到consumer处理的结果，继续生产下一条消息；
					5.	produce决定不生产了，通过c.close()关闭consumer，整个过程结束。
					整个流程无锁，由一个线程执行，produce和consumer协作完成任务，所以称为“协程”，而非线程的抢占式多任务。
					最后套用Donald Knuth的一句话总结协程的特点：
					“子程序就是协程的一种特例。”
	什么是coroutine
			coroutine最大的好处是可以保存堆栈，让程序得以继续执行，在python里面，一般是利用 yield 以及 yield from 语法来实现
			
			coroutine即为一个支持写成的函数，可以利用 iscoroutinefunction 来判断是否coroutine函数，这个函数需要@asyncio.coroutine来修饰
			利用@asyncio.coroutine修饰以后，这个函数可以支持 await(python 3.5) 或者 yield from 语法,一旦执行 yield from 语法以后，asyncio
			将会挂起当前的coroutine，去执行其他的coroutine
	event loop
					asyncio库一个重要的概念就是事件循环，只有启动事件循环以后，才可以让coroutine任务得以继续执行，如果event loop停止或者
					暂停，那么整个异步io也停止或者暂停，类似于操作系统的事件循环机制
					asyncio的内部是基于selector(也可能是epoll)或者windows iocp来实现的，这也是为什么需要启动一个event loop，event loop可以
					成是对各个平台的异步IO"等待"这个操作的封装	 		 
	扩展asyncio
'asyncio库'--基于coroutine的异步O库 -- Python module, Asynchronous I/O, event loop, coroutines and tasks
			Asyncio 本质是消息循环，提供了完善的异步IO支持；
					异步操作需要在coroutine中通过 yield from 完成；
					多个coroutine可以封装成一组Task然后并发执行。
					yield from 语法可以让我们方便地调用另一个generator					
			asyncio的编程模型就是一个消息循环。我们从asyncio模块中直接获取一个EventLoop的引用，然后把需要执行的协程扔到EventLoop中执行，就实现了异步IO。
				用asyncio实现Hello world代码如下：
					import asyncio					

					@asyncio.coroutine 
					def hello():
					    print("Hello world!")
					    # 异步调用asyncio.sleep(1):
					    r = yield from asyncio.sleep(1) 
					    print("Hello again!")					

					# 获取EventLoop:
					loop = asyncio.get_event_loop()
					# 执行coroutine
					loop.run_until_complete(hello())
					loop.close()
				代码解读
					@asyncio.coroutine把一个generator标记为coroutine类型，然后，我们就把这个coroutine扔到EventLoop中执行。
					hello()会首先打印出Hello world!，然后，yield from 语法可以让我们方便地调用另一个generator。由于asyncio.sleep()也是一个coroutine，
					所以线程不会等待asyncio.sleep()，而是直接中断并执行下一个消息循环。当asyncio.sleep()返回时，线程就可以从yield from拿到返回值
					（此处是None），然后接着执行下一行语句。
					把asyncio.sleep(1)看成是一个耗时1秒的IO操作，在此期间，主线程并未等待，而是去执行EventLoop中其他可以执行的coroutine了，因此
					可以实现并发执行。
				我们用Task封装两个coroutine试试：
					import threading
					import asyncio					

					@asyncio.coroutine
					def hello():
					    print('Hello world! (%s)' % threading.currentThread())
					    yield from asyncio.sleep(1)
					    print('Hello again! (%s)' % threading.currentThread())					

					loop = asyncio.get_event_loop()
					tasks = [hello(), hello()]
					loop.run_until_complete(asyncio.wait(tasks))
					loop.close()
				观察执行过程：
					Hello world! (<_MainThread(MainThread, started 140735195337472)>)
					Hello world! (<_MainThread(MainThread, started 140735195337472)>)
					(暂停约1秒)
					Hello again! (<_MainThread(MainThread, started 140735195337472)>)
					Hello again! (<_MainThread(MainThread, started 140735195337472)>)
				代码解读
					由打印的当前线程名称可以看出，两个coroutine是由同一个线程并发执行的。
					如果把asyncio.sleep()换成真正的IO操作，则多个coroutine就可以由一个线程并发执行。
				我们用asyncio的异步网络连接来获取sina、sohu和163的网站首页：
					import asyncio					

					@asyncio.coroutine
					def wget(host):
					    print('wget %s...' % host)
					    connect = asyncio.open_connection(host, 80)
					    reader, writer = yield from connect
					    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
					    writer.write(header.encode('utf-8'))
					    yield from writer.drain()
					    while True:
					        line = yield from reader.readline()
					        if line == b'\r\n':
					            break
					        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
					    # Ignore the body, close the socket
					    writer.close()					

					loop = asyncio.get_event_loop()
					tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
					loop.run_until_complete(asyncio.wait(tasks))
					loop.close()
				执行结果如下：
					wget www.sohu.com...
					wget www.sina.com.cn...
					wget www.163.com...
					(等待一段时间)
					(打印出sohu的header)
					www.sohu.com header > HTTP/1.1 200 OK
					www.sohu.com header > Content-Type: text/html
					...
					(打印出sina的header)
					www.sina.com.cn header > HTTP/1.1 200 OK
					www.sina.com.cn header > Date: Wed, 20 May 2015 04:56:33 GMT
					...
					(打印出163的header)
					www.163.com header > HTTP/1.0 302 Moved Temporarily
					www.163.com header > Server: Cdn Cache Server V2.0
					...
				代码解读	
					writer.drain()刷新底层传输的写缓冲区。也就是把需要发送出去的数据，从缓冲区发送出去。没有手工刷新，asyncio为你自动刷新了。
					当执行到reader.readline()时，asyncio知道应该把发送缓冲区的数据发送出去了。
					可见3个连接由一个线程通过coroutine并发完成。
			小结
					asyncio提供了完善的异步IO支持；
					异步操作需要在coroutine中通过yield from完成；
					多个coroutine可以封装成一组Task然后并发执行。
			参考源码
					async_hello.py
					async_wget.py
'async/(await/return)'--代替@asyncio.coroutine和 yield from --使被装饰函数变成协程函数--关键字 await 只能在 async def 函数中使用
	用asyncio提供的@asyncio.coroutine可以把一个generator标记为coroutine类型，然后在coroutine内部用 yield from 调用另一个coroutine实现异步操作。			
	为了简化并更好地标识异步IO，从Python 3.5开始引入了新的语法async和await，可以让coroutine的代码更简洁易读。
		请注意，async和await是针对coroutine的新语法，要使用新的语法，只需要做两步简单的替换：
					1.	把@asyncio.coroutine替换为async；
					2.	把yield from替换为await。
		让我们对比一下上一节的代码：
					@asyncio.coroutine
					def hello():
					    print("Hello world!")
					    r = yield from asyncio.sleep(1)
					    print("Hello again!")
		用新语法重新编写如下：
					async def hello():
					    print("Hello world!")
					    r = await asyncio.sleep(1)
					    print("Hello again!")
		剩下的代码保持不变。
	小结
		Python从3.5版本开始为asyncio提供了async和await的新语法；
		注意新语法只能用在Python 3.5以及后续版本，如果使用3.4版本，则仍需使用上一节的方案。
		async和await是Python 3.5中新添加的关键词，用来定义一个原生的协程，以便于和基于协程的生成器相区别。如果你想了解更多
		关于async和await的知识，你可以去阅读PEP 492。
		在Python 3.4中，你可以按照如下方式创建一个协程，
					import asyncio					

					@asyncio.coroutine
					def my_foo():
					    yield from func()
		这个装饰器在Python 3.5中依然有效，但是模块的类型有所更新，协程函数可以告诉你正在交互的是不是一个原生的协程。从Python 3.5
		开始，你可以使用async def这种语法来定义一个协程函数，所以上述函数可以按照如下方式定义，
					import asyncio					

					async def my_coro():
					    await func()
		当你以这种方式定义一个协程函数，你不能在函数内部使用 yield。取而代之，你必须使用 return 或者 await 语句，用于将返回值返回给调用者。
		你需要注意的是，关键字 await 只能在 async def 函数中使用。
					关键字 async 和 await 可以认为是异步编程中的接口。asyncio模块就是一个可以将 async/await 用于异步编程的框架。实
	协程示例
		一个非常常见的任务就是你想完整的下载一个文件，这个文件可能来源于内部资源或者互联网。当然你想要下载的文件可能不止一个。让我们
		创建两个协程来完成这个任务。
			代码如下
					import asyncio
					import os
					import urllib.request					

					async def download_coroutine(url):
					    request = urllib.request.urlopen(url)
					    filename = os.path.basename(url)					

					    with open(filename,"wb") as file_handle:
					        while True:
					            chunk = request.read(1024)
					            if not chunk:
					                break
					            file_handle.write(chunk)
					        msg = "Finished downloading {filename}".format(filename = filename)
					        return msg					

					async def main(urls):
					    coroutines = [download_coroutine(url) for url in urls]
					    completed,pending = await asyncio.wait(coroutines)
					    for item in completed:
					        print(item.result())					

					if __name__ == "__main__":
					    urls = ["http://www.irs.gov/pub/irs-pdf/f1040.pdf",
					            "http://www.irs.gov/pub/irs-pdf/f1040a.pdf",
					            "http://www.irs.gov/pub/irs-pdf/f1040ez.pdf",
					            "http://www.irs.gov/pub/irs-pdf/f1040es.pdf",
					            "http://www.irs.gov/pub/irs-pdf/f1040sb.pdf"]
					    event_loop = asyncio.get_event_loop()
					    try:
					        event_loop.run_until_complete(main(urls))
					    finally:
					        event_loop.close()
			代码解读
					这段代码中，我们引入了我们需要的模块，然后通过async语法创建了第一个协程。这个协程叫做download_coroutine，它使用Python的
					urllib模块下载传递给它的任何URL地址。当它完成任务时，它将会返回一条相应的信息。
					另一个协程就是我们的主协程。它基本上就是获取一个包含一个或者多个URL地址的列表，然后将它们加入队列。我们使用asyncio的wait
					函数用于等待协程的结束。当然，为了启动这些协程，它们需要被加入到事件循环中。我们在代码段中最后的地方做了这个处理，我们先获取
					一个事件循环，然后调用它的run_until_complete的方法。你将会注意到，我们将主协程传入事件循环中。这个会先运行主协程，主协程将
					第二个协程加入到队列中，并让它们运行。这就是有名的链协程。
	调度调用--通过异步事件循环来调度调用常规函数
				第一个方法是call_soon。方法call_soon基本上就是尽可能的调用你的回调或者事件句柄。它的工作机制类似于先进先出队列，所以如果
				一些回调需要一段时间来处理任务，其它的回调就会相应的延迟，直到先前的回调结束。
				让我们来看一个示例。
					import asyncio
					import functools					

					def event_handler(loop,stop = False):
					    print("Event handler called")
					    if stop:
					        print("Stopping the loop")
					        loop.stop()					

					if __name__ == "__main__":
					    loop = asyncio.get_event_loop()
					    try:
					        loop.call_soon(functools.partial(event_handler,loop))
					        print("Starting event loop")
					        loop.call_soon(functools.partial(event_handler,loop,stop = True))					

					        loop.run_forever()
					    finally:
					        print("closing event loop")
					        loop.close()
				代码解读
					由于asyncio的函数不接受关键字，但是如果我们需要将关键字传入事件句柄中，那么我们就需要使用functools模块了。无论何时被
					调用，我们定义的常规函数将会在标准输出上打印一些文字信息。如果你偶然将这个函数的stop变量设置为True，它将会停止事件循环。
					第一次我们调用它时，我们没有停止事件循环。第二次我们调用它时，我们停止了事件循环。我们停止事件循环的原因是我们将它放入
					run_forever，这个将时间循环设置为无限循环。一旦循环停止，我们就可以将它关闭。如果你运行这段代码，你得到的输出如下所示，
					Starting event loop
					Event handler called
					Event handler called
					Stopping the loop
					closing event loop
					还有一个相关的函数是call_soon_threadsafe，顾名思义，它与call_soon的工作机制相似，但是它是线程安全的。
					如果你想延迟一段时间再调用，你可以使用call_later函数。在这个示例中，我们可以将call_soon函数按照如下方式修改，
					loop.call_later(1,event_handler,loop)
					这个将会延迟调用我们的事件句柄1秒钟，然后才会去调用它，并将循环作为第一个参数传入。
					如果你想在未来一个指定的时间调度，你需要获取循环的时间，而不是计算机的时间，你可以按照如下方式操作，
					current_time = loop.time()
					一旦你这样做，你可以使用call_at函数，然后将你想调用事件句柄的时间传递给它。让我们来看看我们想在5分钟之后调用我们的
					事件句柄，下面就是你如何操作的，
					loop.call_at(current_time + 300,event_handler,loop)
					在这个示例中，我们使用我们获取的当前时间，然后加上300秒钟或者5分钟。通过这个操作，我们延迟调用事件循环5分钟。
				

	练习
					将上一节的异步获取sina、sohu和163的网站首页源码用新语法重写并运行。
	参考源码
					async_hello2.py
					async_wget2.py
'aiohttp'-协程网络IO(异步网络IO，async+io+http)--aiohttp则是基于asyncio实现的HTTP框架--用单线程+coroutine实现多用户的高并发支持
	asyncio可以实现单线程并发IO操作。如果仅用在客户端，发挥的威力不大。
	如果把asyncio用在服务器端，例如Web服务器，由于HTTP连接就是IO操作，因此可以用单线程+coroutine实现多用户的高并发支持。
	asyncio实现了TCP、UDP、SSL等协议，aiohttp则是基于asyncio实现的HTTP框架。
	我们先安装aiohttp：pip install aiohttp
	然后编写一个HTTP服务器，分别处理以下URL：
				•	/ - 首页返回b'<h1>Index</h1>'；
				•	/hello/{name} - 根据URL参数返回文本hello, %s!。
				代码如下：
				import asyncio				
				from aiohttp import web				

				async def index(request):
				    await asyncio.sleep(0.5) # 模拟IO阻塞
				    return web.Response(body=b'<h1>Index</h1>', content_type='text/html')				

				async def hello(request):
				    await asyncio.sleep(0.5) # 模拟IO阻塞
				    text = '<h1>hello, %s!</h1>' % request.match_info['name']
				    return web.Response(body=text.encode('utf-8'), content_type='text/html')				

				async def init(loop):
				    app = web.Application(loop=loop)
				    app.router.add_route('GET', '/', index)
				    app.router.add_route('GET', '/hello/{name}', hello)
				    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)
				    print('Server started at http://127.0.0.1:8000...')
				    return srv				

				loop = asyncio.get_event_loop()
				loop.run_until_complete(init(loop))
				loop.run_forever()
				注意aiohttp的初始化函数init()也是一个coroutine，loop.create_server()则利用asyncio创建TCP服务。
	参考源码
				aio_web.py
 