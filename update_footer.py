import os
files = ['services.html', 'pricing.html', 'index.html', 'home-2.html', 'faq.html', 'contact.html', 'blog.html', 'about.html']

target = '''            <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 mb-10 pt-4">
                <div class="lg:col-span-4">
                    <div class="mb-6">
                        <a href="index.html" class="inline-flex items-center gap-3 text-2xl font-bold tracking-widest uppercase"
                            style="color: var(--text-main) !important; text-decoration: none;">
                            <i class="fas fa-book-open" style="color: var(--accent-color); font-size: 1.4rem;"></i>
                            LibroSpace
                        </a>
                    </div>
                    <p class="opacity-80 leading-relaxed text-sm font-medium mb-8 max-w-sm" style="color: var(--text-muted);">
                        Dedicated to providing the ultimate reading experience. Whether you are looking for a permanent addition to your shelf or a weekend escape, we have a book waiting for you.
                    </p>
                    <div class="flex space-x-4">
                        <a href="#" class="social-link-circle"><i class="fab fa-instagram"></i></a>
                        <a href="#" class="social-link-circle"><i class="fab fa-facebook-f"></i></a>
                        <a href="#" class="social-link-circle"><i class="fab fa-x-twitter"></i></a>
                        <a href="#" class="social-link-circle"><i class="fab fa-whatsapp"></i></a>
                    </div>
                </div>
                
                <div class="lg:col-span-8">
                    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-10">
                        <div>
                            <h4>Reader Portal</h4>
                            <ul class="space-y-4">
                                <li><a href="login.html">Member Login</a></li>
                                <li><a href="user.html">Reading Dashboard</a></li>
                                <li><a href="#">My Borrowed Books</a></li>
                                <li><a href="pricing.html">Lending Plans</a></li>
                                <li><a href="faq.html">Library FAQ</a></li>
                            </ul>
                        </div>
                        <div>
                            <h4>Our Catalog</h4>
                            <ul class="space-y-4">
                                <li><a href="services.html">New Releases</a></li>
                                <li><a href="services.html">Fiction & Literature</a></li>
                                <li><a href="services.html">Non-Fiction & Bio</a></li>
                                <li><a href="services.html">Children's Books</a></li>
                                <li><a href="services.html">Rare Collections</a></li>
                            </ul>
                        </div>
                        <div class="sm:col-span-2 md:col-span-1">
                            <h4>Main Library</h4>
                            <ul class="space-y-4 text-[var(--text-muted)] text-sm font-medium">
                                <li class="flex items-start gap-4">
                                    <i class="fas fa-map-marker-alt mt-1 shrink-0" style="color: var(--accent-color);"></i>
                                    <span>221B Baker Street<br>Literary District, LDN</span>
                                </li>
                                <li class="flex items-center gap-4">
                                    <i class="fas fa-phone shrink-0" style="color: var(--accent-color);"></i>
                                    <a href="tel:+15550198" class="break-all hover:text-[var(--accent-color)]">+1 (555) 800-READ</a>
                                </li>
                                <li class="flex items-center gap-4">
                                    <i class="fas fa-envelope shrink-0" style="color: var(--accent-color);"></i>
                                    <a href="contact.html" class="break-all hover:text-[var(--accent-color)]">hello@librospace.com</a>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="footer-bottom flex flex-col md:flex-row justify-between items-center text-xs gap-6 font-semibold uppercase tracking-widest">'''

replacement = '''            <div class="grid grid-cols-1 xl:grid-cols-12 gap-12 xl:gap-16 mb-10 pt-4">
                <div class="xl:col-span-4 flex flex-col items-center xl:items-start text-center xl:text-left">
                    <div class="mb-6">
                        <a href="index.html" class="inline-flex items-center gap-3 text-2xl font-bold tracking-widest uppercase"
                            style="color: var(--text-main) !important; text-decoration: none;">
                            <i class="fas fa-book-open" style="color: var(--accent-color); font-size: 1.4rem;"></i>
                            LibroSpace
                        </a>
                    </div>
                    <p class="opacity-80 leading-relaxed text-sm font-medium mb-8 max-w-sm mx-auto xl:mx-0" style="color: var(--text-muted);">
                        Dedicated to providing the ultimate reading experience. Whether you are looking for a permanent addition to your shelf or a weekend escape, we have a book waiting for you.
                    </p>
                    <div class="flex space-x-4 justify-center xl:justify-start">
                        <a href="#" class="social-link-circle"><i class="fab fa-instagram"></i></a>
                        <a href="#" class="social-link-circle"><i class="fab fa-facebook-f"></i></a>
                        <a href="#" class="social-link-circle"><i class="fab fa-x-twitter"></i></a>
                        <a href="#" class="social-link-circle"><i class="fab fa-whatsapp"></i></a>
                    </div>
                </div>
                
                <div class="xl:col-span-8">
                    <div class="grid grid-cols-1 sm:grid-cols-3 gap-10 text-center sm:text-left">
                        <div>
                            <h4>Reader Portal</h4>
                            <ul class="space-y-4 inline-block sm:block text-left">
                                <li><a href="login.html">Member Login</a></li>
                                <li><a href="user.html">Reading Dashboard</a></li>
                                <li><a href="#">My Borrowed Books</a></li>
                                <li><a href="pricing.html">Lending Plans</a></li>
                                <li><a href="faq.html">Library FAQ</a></li>
                            </ul>
                        </div>
                        <div>
                            <h4>Our Catalog</h4>
                            <ul class="space-y-4 inline-block sm:block text-left">
                                <li><a href="services.html">New Releases</a></li>
                                <li><a href="services.html">Fiction & Literature</a></li>
                                <li><a href="services.html">Non-Fiction & Bio</a></li>
                                <li><a href="services.html">Children's Books</a></li>
                                <li><a href="services.html">Rare Collections</a></li>
                            </ul>
                        </div>
                        <div>
                            <h4>Main Library</h4>
                            <ul class="space-y-4 text-[var(--text-muted)] text-sm font-medium inline-block sm:block text-left">
                                <li class="flex items-start gap-4">
                                    <i class="fas fa-map-marker-alt mt-1 shrink-0" style="color: var(--accent-color);"></i>
                                    <span>221B Baker Street<br>Literary District, LDN</span>
                                </li>
                                <li class="flex items-center gap-4">
                                    <i class="fas fa-phone shrink-0" style="color: var(--accent-color);"></i>
                                    <a href="tel:+15550198" class="break-all hover:text-[var(--accent-color)]">+1 (555) 800-READ</a>
                                </li>
                                <li class="flex items-center gap-4">
                                    <i class="fas fa-envelope shrink-0" style="color: var(--accent-color);"></i>
                                    <a href="contact.html" class="break-all hover:text-[var(--accent-color)]">hello@librospace.com</a>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="footer-bottom flex flex-col md:flex-row justify-between items-center text-xs gap-6 font-semibold uppercase tracking-widest text-center md:text-left">'''

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    if target in content:
        content = content.replace(target, replacement)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Updated {file}')
    else:
        print(f'Target not found in {file}')
